#!/bin/bash

# Determine the directory of the shell script
script_dir=$(dirname "$0")
# Define relative paths based on the script's location
movies_script="$script_dir/movies/manage-movie.py"
series_script="$script_dir/series/manage-episode.py"

file_type=$1
file_source=$2
file_name=$3

if [ "$file_type" == "Movies" ]; then
    python $movies_script "$file_source" "$file_name"
elif [ "$file_type" == "Series" ]; then
    python $series_script "$file_source" "$file_name"
else
    echo "Unknown file type: $file_type"
fi

#python /home/pi/manage_torrent.py "$file_type" "$file_source" "$file_name"
