# YT_Playlist_Downloader
This repository consists of python scripts which can download a playlist or a set of videos from YouTube directly from command line.

Inorder to setup the code follow below steps:
---------------------------------------------

 1. Clone the repository in your local machine.
 2. Open the folder and open termianl in current working directory.
 3. Install all the packages mentioned in requirements.txt.
 4. Use the below command to install all packages.

     command:  pip3 install -r requirements.txt

 5. Now the setup is ready, you can download the playlist or list of videos using below steps. 

Download Playlist:
------------------

If you want to download playlist from the YouTube follow the below steps:

 1. Go to the playlist directory.
 2. Open the terminal in the current directory(playlist).
 3. Enter the command in the below format:
	
	python3 playlist_download.py [playlist_url] [directory_path]

 4. If you want to downoad the playlist in the current working directory then there is no need to give directory path in the command.


Download list of videos:
------------------------

If you want to download a set of videos from the You Tube follow the below steps:

 1. Go to the directory "videos".
 2. Save all urls of the videos in the "links.txt" file(Each url in a newline).
 3. Open terminal in current working directory.
 4. Enter the below command.
    command: python3 videos_download.py
 5. You will see 2 options 360 and 720 in the termial.
 6. Select 1 or 2 based on the quality with which you want to download all videos.
 7. All videos will be downloaded in the current directory.

