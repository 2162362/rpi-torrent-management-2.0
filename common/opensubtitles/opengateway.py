import sys
import os
import requests
import json

from dotenv import load_dotenv

load_dotenv()

env_username = os.getenv('OPEN_SUBTITLES_USERNAME')
env_password = os.getenv('OPEN_SUBTITLES_PASSWORD')
env_api_key = os.getenv('OPEN_SUBTITLES_API_KEY')
env_user_agent = os.getenv('OPEN_SUBTITLES_USER_AGENT')

# unnecessary but may be modified later
username = f'{env_username}'
password = f'{env_password}'
api_key = f'{env_api_key}'
user_agent = f'{env_user_agent}'

def login():

    url = 'https://api.opensubtitles.com/api/v1/login'
    body = {'username': username, 'password': password}
    headers = {'User-Agent': user_agent,'Content-Type': 'application/json', 'Accept': "application/json", 'Api-Key': api_key}
    login_response = requests.post(url, data=json.dumps(body), headers=headers)
    if login_response.status_code == 200:
        return login_response.json()['token']
    else:
        print(f"Request failed with status code {login_response.status_code}")
        return None

def load_data(file_name):

    url = f'https://api.opensubtitles.com/api/v1/utilities/guessit?filename={file_name}'
    login_headers = {'User-Agent': user_agent,'Content-Type': 'application/json', 'Accept': "application/json", 'Api-Key': api_key}
    
    login_response = requests.get(url, headers=login_headers)
    if login_response.status_code == 200:
            return login_response.json()
    else:
        print(f"Request failed with status code {login_response.status_code}")
        return None

def get_subtitle_by_query(query_params, language):
    """
    Searches for subtitles on OpenSubtitles API based on the given query and language.

    Args:
        query (str): The search query for the subtitles.
        language (str): The language code for the subtitles.

    Returns:
        dict or None: A dictionary containing the subtitle information if found, otherwise None.
    """

    url = f'https://api.opensubtitles.com/api/v1/subtitles?'
    headers = {'User-Agent': user_agent,'Content-Type': 'application/json', 'Accept': "application/json", 'Api-Key': api_key}
    query = {'query' : query_params['title'], 'year' : query_params['year'], 'languages': language, 'order_by': 'download_count', 'order_direction': 'desc'}
    
    response = requests.get(url, headers=headers, params=query)
    if response.status_code == 200:
        if response.json()['total_count'] > 0:
            return response.json()['data'][0]
        return None
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def download_subtitles(subtitle_id, destination):
    """
    Downloads subtitles for a given subtitle ID and saves them to the specified destination.

    Args:
        subtitle_id (str): The ID of the subtitle to download.
        destination (str): The file path to save the downloaded subtitle to.

    Returns:
        None
    """

    url = f'https://api.opensubtitles.com/api/v1/download'
    
    api_token = login()
    
    headers = {'User-Agent': user_agent,'Content-Type': 'application/json', 'Accept': "application/json", 'Api-Key': api_key, 'Authorization': f'Bearer {api_token}'}
    body = {'file_id': subtitle_id}

    response = requests.post(url, data=json.dumps(body), headers=headers)
    download_link = response.json()['link']
    subtitle_binary = requests.get(download_link).content
    print(destination)
    with open(destination, 'wb') as f:
        f.write(subtitle_binary)
 