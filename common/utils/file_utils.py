import sys
import os
from fuzzywuzzy import fuzz

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../opensubtitles')))
import opengateway

def guess_file_info(file_name):
    """
    Guesses information about a file based on its name.
    It has a very powerful matcher that allows to guess properties from a video using its filename only. This matcher works with both movies and tv shows episodes.
    This is a simple implementation of the python guessit library. https://doc.guessit.io

    Args:
        file_name (str): The name of the file.

    Returns:
        dict: A dictionary containing information about the file, including its name, size, and type.
    """
    return opengateway.load_data(file_name)
    

def find_media_file_with_fuzzy_matching(directory, target_name, threshold=80):
    """
    Searches for media files in the specified directory using fuzzy string matching.

    Args:
        directory (str): The directory to search for media files.
        target_name (str): The name of the media file to search for.
        threshold (int, optional): The minimum similarity threshold for a match. Defaults to 80.

    Returns:
        list: A list of file paths that match the target name with a similarity score greater than or equal to the threshold.
    """
    matching_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Perform fuzzy string matching between the target name and the file name
            similarity = fuzz.ratio(target_name.lower(), file.lower())
            
            # Adjust the threshold as needed; the default is 80 for a decent match
            if similarity >= threshold:
                matching_files.append(os.path.join(root, file))

    return matching_files

def modify_file_extension(file_name: str, substring: str, new_file_extension: str = None) -> str:
    """
    Inserts a substring before the file extension in the given file name.

    Args:
        file_name (str): The name of the file.
        substring (str): The substring to insert before the file extension.
        new_file_extension (str, optional): The new file extension to use. Defaults to None.

    Returns:
        str: The updated file name with the substring inserted before the file extension.
    """
    file_name_without_extension = os.path.splitext(file_name)[0]
    file_extension = os.path.splitext(file_name)[1]
    if new_file_extension:
        file_extension = new_file_extension
    return f"{file_name_without_extension}{substring}{file_extension}"