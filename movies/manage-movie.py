import sys
import os
import datetime
import json
import re
from opensubtitles import managesubtitles

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common/utils')))
import file_utils

def copy_file(file_source):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    with open(os.path.join(parent_dir ,"appsettings.json")) as f:
        config = json.load(f)

    # Escape the file source to handle spaces
    file_source = re.escape(file_source)

    destination = config["directories"]["movies"]
    os.system(f"cp -r {file_source} {destination}")

def get_subtitles(file_source, file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    with open(os.path.join(parent_dir ,"appsettings.json")) as f:
        config = json.load(f)

    destination = os.path.join(config["directories"]["movies"], file_name)

    media_file = file_utils.find_media_file_with_fuzzy_matching(destination, file_name)[0]

    file_id = managesubtitles.search_subtitles(file_name, "pt-PT")
    if file_id is not None:
        modified_media_file = file_utils.modify_file_extension(media_file, ".pt", ".srt")
        managesubtitles.download_subtitles(file_id, modified_media_file)

    file_id = managesubtitles.search_subtitles(file_name, "en")
    if file_id is not None:
        modified_media_file = file_utils.modify_file_extension(media_file, ".en", ".srt")
        managesubtitles.download_subtitles(file_id, modified_media_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python managesubtitle_torrent.py <file_source> <file_name>")
        sys.exit(1)
    try:
        file_source = sys.argv[1]
        file_name = sys.argv[2]
        copy_file(file_source)
        #get_subtitles(file_source, file_name)
    except Exception as e:
        print(e)