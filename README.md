# Raspberry Pi Torrent Management 2.0
This repository serves as a torrent manager for your Raspberry Pi using qBittorrent. It automatically organizes downloaded content into appropriate directories and uses the *OpenSubtitles API* to download subtitles automatically.

## System Requirements
- Raspberry Pi (any model capable of running Python and qBittorrent)
- Python installed
- qBittorrent installed

To ensure smooth operations, it is essential to grant the necessary permissions to the qBittorrent system user for specific files and directories. Follow the instructions below to set up the required permissions:

```bash
sudo usermod -a -G qbittorrent pi
```
### Permissions
Ensure that the qBittorrent system user (qbittorrent) has the appropriate permissions for the following:

- Git Repository:
Grant read and execute permissions to the qBittorrent system user for the repository.

- Movies Directory:
Grant read and write permissions to the qBittorrent system user for the movies directory.

- TV Shows Directory:
Grant read and write permissions to the qBittorrent system user for the TV shows directory.

- Log File:

Grant read and write permissions to the qBittorrent system user for the log file.

### Installing Necessary Packages
Use the following pip commands to install the required Python packages:

```bash
sudo pip install fuzzywuzzy  # Fuzzy string matching for copying TV show files
sudo pip install requests     # Simple HTTP library for fetching movie subtitles
sudo pip install jsonlib       # Load script settings from JSON
sudo pip install regex         # Handle special characters and spaces when copying files
sudo pip install python-dotenv # Load environment variables from .env file
```

You can also install all packages at once with:

```bash
sudo pip install fuzzywuzzy requests jsonlib regex python-dotenv
```

These packages are crucial for the proper functioning of the torrent management system. Make sure that the **python** and **pip** commands installed on your system are for the same version of Python.

**Note:** Ensure that your system has Python and **pip** installed before running the above commands.

### Configuration and Setup
With the permissions set and packages installed, follow these steps to set up the torrent management system:

1. Clone or copy this repository to your desired location on the Raspberry Pi.
2. Configure `appsettings.json` with the correct folders for your media:
```json
{
    "directories":{
        "movies": "/path/to/your/movies",
        "tvshows": "/path/to/your/series",
        "logs": "/path/to/your/logs.txt"
    }
}
```
3. Create a `.env` file in the project's root with your OpenSubtitles API credentials:
```
# environment variables
OPEN_SUBTITLES_USERNAME = "your_username"
OPEN_SUBTITLES_PASSWORD = "your_password"
OPEN_SUBTITLES_API_KEY = "your_api_key"
OPEN_SUBTITLES_USER_AGENT = "your_user_agent"
```
4. Install and configure qBittorrent if you haven't already.
5. Inside qBittorrent interface, create the following categories: "Movies", "Series", and optionally "Games".
6. Configure qBittorrent to run the external program on torrent completion:
   - Go to Tools > Options > Downloads
   - Scroll down to "Run external program on torrent completion"
   - Enter: `/usr/bin/bash /path/to/manage_torrent.sh "%L" "%R" "%N"`
   - Replace `/path/to/manage_torrent.sh` with the actual path to the script in your system

![Qbittorrent external configuration](https://github.com/2162362/rpi-torrent-management-2.0/assets/44852796/d3e95396-cd3b-4b97-8786-f3a20053c9b2)

7. Press "Save"

### Usage
1. When downloading a torrent in qBittorrent, select the appropriate category ("Movies", "Series", or "Games").
2. The torrent will automatically download and be organized into the specified directory from *appsettings.json*.
3. For movies, the system will attempt to download subtitles in Portuguese and English automatically.
4. For TV series, episodes will be organized into appropriate season folders.
5. For games, the system will log the download but won't perform additional organization.

### Contribution
Feel free to contribute to the improvement of this torrent management system. Submit issues, pull requests, or feature suggestions to enhance the functionality and usability.

Happy torrenting!
