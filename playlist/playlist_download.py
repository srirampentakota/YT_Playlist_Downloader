import urllib.request
import urllib.error

import re
import sys
import time
import os

from pytube import YouTube


def getPageHtml(url):
    try:
        yTUBE = urllib.request.urlopen(url).read()
        return str(yTUBE)
    except urllib.error.URLError as e:
        print(e.reason)
        exit(1)

def getPlaylistUrlID(url):
    if 'list=' in url:
        eq_idx = url.index('=') + 1
        pl_id = url[eq_idx:]
        if '&' in url:
            amp = url.index('&')
            pl_id = url[eq_idx:amp]
        return pl_id   
    else:
        print(url, "is not a youtube playlist.")
        exit(1)

def getFinalVideoUrl(vid_urls):
	final_urls = []
	for vid_url in vid_urls:
		url_amp = len(vid_url)
		if '&' in vid_url:
			url_amp = vid_url.index('&')
		final_urls.append('http://www.youtube.com/' + vid_url[:url_amp])
	#final_urls.sort()
	return final_urls

def getPlaylistVideoUrls(page_content, url):
	playlist_id = getPlaylistUrlID(url)
	#print(playlist_id)

	vid_url_pat = re.compile(r'watch\?v=\S+?list=' + playlist_id)
	vid_url_matches = list(set(re.findall(vid_url_pat, page_content)))

	if vid_url_matches:
		final_vid_urls = getFinalVideoUrl(vid_url_matches)
		#final_vid_urls.sort()
		Tot_files=len(final_vid_urls)
		print("Found",Tot_files,"videos in playlist.")
		printUrls(final_vid_urls)
		return final_vid_urls
	else:
		print('No videos found.')
		exit(1)



#function added to get audio files along with the video files from the playlist

def download_Video_Audio(path, vid_url, file_no):
    yt=YouTube(url=vid_url)
    try:  
        # searches for a video in 720p
        video=yt.streams.filter(progressive=True, file_extension='mp4',resolution='720p').order_by('resolution').asc().first()
    except Exception:  
        # Sorts videos by resolution and picks the highest quality video if a 720p video doesn't exist
        video=yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    try:
        if(os.path.isfile(video.default_filename)):
            print(video.default_filename, "already exists in this directory! Skipping video...")
        else:
            print("download started:  ", video.default_filename)
            video.download(path)
            print("successfully downloaded", video.default_filename, "!")
    except OSError:
        print(video.default_filename, "already exists in this directory! Skipping video...")

def printUrls(vid_urls):
    for url in vid_urls:
        print(url)
        time.sleep(0.04)
        
if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('USAGE: python3 playlist_download.py playlistURL OR python3 playlist_download.py playlistURL destPath')
        exit(1)
    else:
        url = sys.argv[1]
        directory = os.getcwd() if len(sys.argv) != 3 else sys.argv[2]
    
        # make directory if dir specified doesn't exist
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError as e:
            print(e.reason)
            exit(1)

        if not url.startswith("http"):
            url = 'https://' + url

        playlist_page_content = getPageHtml(url)
        vid_urls_in_playlist = getPlaylistVideoUrls(playlist_page_content, url)

        # downloads videos and audios
        for i,vid_url in enumerate(vid_urls_in_playlist):
            download_Video_Audio(directory, vid_url, i)
time.sleep(1)
        
