#!/usr/bin/python

import os
import datetime

from pytube import YouTube, Playlist

WORKSPACE = os.getcwd()

YOUTUBE_URL = 'https://www.youtube.com/watch?v='
FORMAT='mp4'
DEFAULT_RESOLUTION='480p'
# FOR YOUTUBE VIDEO
######################################################
    
class YouTubeVideo:

    def __init__(self, youtube_id):
        self.youtube_id = youtube_id

    def download_video_with_audio(self, resolution=None):
        youtube_video = YouTube(YOUTUBE_URL + self.youtube_id)
        videos = youtube_video.streams.filter(progressive=True, resolution=resolution)
        for video in videos:
            print(video)


    def dowload_video(self, resolution=None):
        youtube_video = YouTube(YOUTUBE_URL + self.youtube_id)
        videos = youtube_video.streams.filter(resolution=resolution)
        for video in videos:
            print(video)


    def dowload_audio(self):
        youtube_video = YouTube(YOUTUBE_URL + self.youtube_id)
        videos = youtube_video.streams.filter(only_audio=True)
        for video in videos:
            print(video)


    def get_title(self):
        youtube_video = YouTube(YOUTUBE_URL + self.youtube_id)
        return youtube_video.title


    def get_duration(self):
        youtube_video = YouTube(YOUTUBE_URL + self.youtube_id)
        return str(datetime.timedelta(seconds=youtube_video.length))

# FOR YOUTUBE PLAYLIST
######################################################
def download_playlist(yt_playlist_id):
    youtube_playlist = Playlist(YOUTUBE_URL + yt_playlist_id)
    print(f'Downloading {youtube_playlist.title}')
    for video in youtube_playlist.videos:
        video.streams.first().download()

if __name__ == '__main__':
    EXAMPLE_ID = '-mdv2wf8yQ8'
    k = YouTubeVideo(EXAMPLE_ID)
    print(k.get_title())
    print(k.get_duration())
    k.dowload_audio()
