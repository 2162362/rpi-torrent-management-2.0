import sys
import os
import json
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common/utils')))
import file_utils

def copy_file(file_source, destination):
    #strings have to be escaped in case the are spaces in file paths and names
    os.system(f"cp -r \"{file_source}\" \"{destination}\"")

def copy_files_from_folder(folder_source, destination):
    #use wildcard * to copy all files from folder
    os.system(f"cp -r \"{folder_source}\"/* \"{destination}\"")

def get_episode_destination(episode_metadata):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    with open(os.path.join(parent_dir ,"appsettings.json")) as f:
        config = json.load(f)

    tvshow_destination = config["directories"]["tvshows"]
    title = episode_metadata["title"]

    season_number = episode_metadata.get("season")
    if season_number is None:
        season_number = "1"
    season = f'Season {episode_metadata["season"]}'
    directory = os.path.join(tvshow_destination, title, season)

    # Remove or replace disallowed characters
    directory = re.sub(r'[:*?"<>|&%$`]', '', directory)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory

def get_season_destination(episode_metadata):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    with open(os.path.join(parent_dir ,"appsettings.json")) as f:
        config = json.load(f)
        
    tvshow_destination = config["directories"]["tvshows"]
    title = episode_metadata["title"]

    season_number = episode_metadata.get("season")
    if season_number is None:
        season_number = "1"
    season = f'Season {season_number}'
    directory = os.path.join(tvshow_destination, title, season)
    
    # Remove or replace disallowed characters
    directory = re.sub(r'[:*?"<>|&%$`]', '', directory)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python manage-episode.py <file_source> <file_name>")
        sys.exit(1)
    try:
        file_source = sys.argv[1]
        file_name = sys.argv[2]
        episode_metadata = file_utils.guess_file_info(file_name)

        #if downloaded whole season, copy the content as is
        if episode_metadata.get("episode") is None:
            destination = get_season_destination(episode_metadata)
            copy_files_from_folder(file_source, destination)
            
        #if downloaded single episode, copy the content to the episode folder
        else:
            # search for video file inside folde
            if os.path.isdir(file_source):
                file_source = file_utils.find_media_file_with_fuzzy_matching(file_source, file_name)[0]
            destination = get_episode_destination(episode_metadata)
            copy_file(file_source, destination)
    except Exception as e:
        log_file = open("/mnt/mitsai/torrents/logs.txt", "a+")
        log_file.write(str(e))