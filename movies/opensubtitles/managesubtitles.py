import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../common/opensubtitles')))
import opengateway

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../common/utils')))
import file_utils
    
def search_subtitles(file_name, language):
    """
    Searches for subtitles for a given file name and language.

    Args:
        file_name (str): The name of the file to search subtitles for.
        language (str): The language of the subtitles to search for.

    Returns:
        str: The ID of the subtitle file that matches the search query.
    """

    file_metadata = file_utils.guess_file_info(file_name)
    query_params = {
        'title': file_metadata['title'],
        'year': file_metadata['year']
    }
    subtitledata = opengateway.get_subtitle_by_query(query_params, language)
    print(subtitledata['attributes']['files'][0])
    return subtitledata['attributes']['files'][0]['file_id']

def download_subtitles(subtitle_id, destination):
    """
    Downloads subtitles for a given subtitle ID and saves them to the specified destination.

    Args:
        subtitle_id (str): The ID of the subtitle to download.
        destination (str): The path to save the downloaded subtitle file.

    Returns:
        None
    """
    opengateway.download_subtitles(subtitle_id, destination)