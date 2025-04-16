import sys
import os
import json
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common/utils')))
import file_utils

def write_log(message):
    log_file_path = "/mnt/mitsai/torrents/logs.txt"
    with open(log_file_path, "a+") as log_file:
        log_file.write(message + "\n")

def copy_file(file_source, destination):
    try:
        write_log(f"Copying file from {file_source} to {destination}")
        os.system(f"cp -r \"{file_source}\" \"{destination}\"")
    except Exception as e:
        write_log(f"Error copying file: {str(e)}\n{traceback.format_exc()}")

def copy_files_from_folder(folder_source, destination):
    try:
        write_log(f"Copying all files from folder {folder_source} to {destination}")
        os.system(f"cp -r \"{folder_source}\"/* \"{destination}\"")
    except Exception as e:
        write_log(f"Error copying files from folder: {str(e)}\n{traceback.format_exc()}")

def get_episode_destination(episode_metadata):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        with open(os.path.join(parent_dir, "appsettings.json")) as f:
            config = json.load(f)

        tvshow_destination = config["directories"]["tvshows"]
        title = episode_metadata["title"]

        season_number = episode_metadata.get("season", "1")
        season = f'Season {season_number}'
        directory = os.path.join(tvshow_destination, title, season)

        # Remove or replace disallowed characters
        directory = re.sub(r'[:*?"<>|&%$`]', '', directory)

        if not os.path.exists(directory):
            os.makedirs(directory)

        write_log(f"Generated episode destination: {directory}")
        return directory
    except Exception as e:
        write_log(f"Error generating episode destination: {str(e)}\n{traceback.format_exc()}")
        raise

def get_season_destination(episode_metadata):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        with open(os.path.join(parent_dir, "appsettings.json")) as f:
            config = json.load(f)

        tvshow_destination = config["directories"]["tvshows"]
        title = episode_metadata["title"]

        season_number = episode_metadata.get("season", "1")
        season = f'Season {season_number}'
        directory = os.path.join(tvshow_destination, title, season)

        # Remove or replace disallowed characters
        directory = re.sub(r'[:*?"<>|&%$`]', '', directory)

        if not os.path.exists(directory):
            os.makedirs(directory)

        write_log(f"Generated season destination: {directory}")
        return directory
    except Exception as e:
        write_log(f"Error generating season destination: {str(e)}\n{traceback.format_exc()}")
        raise


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python manage-episode.py <file_source> <file_name>")
        sys.exit(1)
        
    try:
        file_source = sys.argv[1]
        file_name = sys.argv[2]
        write_log(f"Script started with file_source: {file_source}, file_name: {file_name}")

        episode_metadata = file_utils.guess_file_info(file_name)
        write_log(f"Guessed episode metadata: {episode_metadata}")

        # If downloaded whole season, copy the content as is
        if episode_metadata.get("episode") is None:
            destination = get_season_destination(episode_metadata)
            copy_files_from_folder(file_source, destination)
        else:
            # Search for video file inside folder
            if os.path.isdir(file_source):
                file_source = file_utils.find_media_file_with_fuzzy_matching(file_source, file_name)[0]

            destination = get_episode_destination(episode_metadata)
            copy_file(file_source, destination)

        write_log(f"Copy operation completed successfully.")
    except Exception as e:
        error_message = f"Unhandled error: {str(e)}\n{traceback.format_exc()}"
        write_log(error_message)
        print(error_message)