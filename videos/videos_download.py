from prettytable import PrettyTable
from pytube import YouTube
import sys
import os

#function added to get audio files along with the video files from the playlist

def download_Video_Audio(path, vid_url, file_no,qua):
    yt=YouTube(url=vid_url)
    if(qua==2):
        try:  # search for video in 720p
            video=yt.streams.filter(progressive=True, file_extension='mp4',resolution='720p').order_by('resolution').asc().first()
        except Exception:
            try:
                # search for video in 360p
                video=yt.streams.filter(progressive=True, file_extension='mp4',resolution='360p').order_by('resolution').asc().first()
              
            except Exception:
                # Sort videos by resolution and picks the highest quality video if a 720p and 360p doesn't exist
                video=yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    else:
        try:  # Search for a video in 360p
            video=yt.streams.filter(progressive=True, file_extension='mp4',resolution='360p').order_by('resolution').asc().first()
        except Exception:
            try:
                video=yt.streams.filter(progressive=True, file_extension='mp4',resolution='720p').order_by('resolution').asc().first()
            except Exception:      
                # Sort videos by resolution and picks the highest quality video if a 360p and 720p videos doesn't exist
                video=yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()        
    try:
        if(os.path.isfile(video.default_filename)):
            print(video.default_filename, "already exists in this directory! Skipping video...")
            return video.default_filename
        else:
            print("download started:  ", video.default_filename)
            video.download(path)
            print("successfully downloaded", video.default_filename, "!")
            return 'None'
    except OSError:
        print(video.default_filename, "already exists in this directory! Skipping video...")
        print(video)
        return video.default_filename

        
if __name__ == '__main__':
    directory = os.getcwd()
    file1=open("links.txt",'r')
    file2=open("failed.txt",'w')
    vid_urls_in_playlist=file1.readlines()
    t = PrettyTable(['url', 'file_name'])
    print("Select Quality:")
    print("1. 360")
    print("2. 720")
    qua=int(input())
    for i,vid_url in enumerate(vid_urls_in_playlist):
        x=download_Video_Audio(directory, vid_url[:-1], i,qua)
        if(x=='None'):
            continue
        else:
            t.add_row([vid_url,x])
    out=t.get_string()
    file2.write(out)
