import sys
import os
import traceback
import json

def write_log(message):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    with open(os.path.join(parent_dir, "appsettings.json")) as f:
        config = json.load(f)
    log_file_path = config["directories"]["logs"]
    with open(log_file_path, "a+") as log_file:
        log_file.write(message + "\n")

def log_game_download(file_source, game_name):
    try:
        write_log(f"Game download logged: Source: {file_source}, Name: {game_name}")
    except Exception as e:
        write_log(f"Error logging game download: {str(e)}\n{traceback.format_exc()}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python manage-game.py <file_source> <game_name>")
        sys.exit(1)

    try:
        file_source = sys.argv[1]
        game_name = sys.argv[2]
        write_log(f"Script started with file_source: {file_source}, game_name: {game_name}")
        log_game_download(file_source, game_name)
        write_log(f"Game download logging completed successfully.")
    except Exception as e:
        error_message = f"Unhandled error: {str(e)}\n{traceback.format_exc()}"
        write_log(error_message)
        print(error_message)
