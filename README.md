# Raspberry Pi Torrent Management 2.0
This repository serves as torrent manager on your Raspberry Pi using qBittorrent. Uses *OpenSubtitles API* to download subtitles automatically.
To ensure smooth operations, it is essential to grant the necessary permissions to the qBittorrent system user for specific files and directories. Follow the instructions below to set up the required permissions:

```
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
These packages are crucial for the proper functioning of the torrent management system.

**Note:** Ensure that your system has Python and **pip** installed before running the above commands.

### Usage
With the permissions set and packages installed, your Raspberry Pi is now ready to efficiently manage torrents using qBittorrent.

1. Copy the package into your system folder.
2. Configure appsettings with correct folders
3. Configure .env file in project's root with correct Opensubtitles API key, username, password and user agent
```
# environment variables
OPEN_SUBTITLES_USERNAME = "--username--"
OPEN_SUBTITLES_PASSWORD = "--password--"
OPEN_SUBTITLES_API_KEY = "--api key---"
OPEN_SUBTITLES_USER_AGENT = "--user agent--"
```
4. Install and configure qBittorrent
5. Inside qBittorrent interface create 2 main categories: Movies and Series
6. Configure qBittorrent to run external program on torrent completion.
![Qbittorrent external configuration](https://github.com/2162362/rpi-torrent-management-2.0/assets/44852796/d3e95396-cd3b-4b97-8786-f3a20053c9b2)
> type in the textbox /usr/bin/bash /path/to/manage_torrent.sh "%L" "%R" "%N"
7. Press "Save"
8. When downloading a torrent select the appropriate category
9. The torrent should automatically download and into specified directory from *appsettings.json*

### Contribution
Feel free to contribute to the improvement of this torrent management system. Submit issues, pull requests, or feature suggestions to enhance the functionality and usability.

Happy torrenting!
