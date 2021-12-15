#!/usr/bin/python
import argparse
import os
import datetime

from pytube import YouTube
from src.fatube.DownloaderHelpers import YTHelper

WORKSPACE = os.getcwd()

YOUTUBE_URL = 'https://www.youtube.com/watch?v='
VIDEO_FORMAT = 'mp4'
DEFAULT_RESOLUTION = '480p'
VIDEO_DIRECTORY='VIDEOS'
AUDIO_DIRECTORY='AUDIO'
VIDEO_AND_AUDIO_DIRECTORY='VIDEO_AUDIO'


class YouTubeVideo:
    """
        The YouTube object is reponsible for connection with YT
        to download videos or audios and obtain desired information
    """
    def __init__(self, youtube_id, video_format):
        """Initializes needed parameters cloesly related to YT service"""
        self.youtube_id = youtube_id
        self.video_format = video_format
        self.youtube_video = YouTube(YOUTUBE_URL + self.youtube_id)

    def download_video(self, video_resolution=None):
        """ Download the video itself"""
        videos = self.youtube_video.streams.filter(
                                            resolution=video_resolution,
                                            only_video=True)
        if video_resolution is not None:
            if not YTHelper.check_empty_list_of_candidates(videos):
                YTHelper.prepare_place_for_download(VIDEO_DIRECTORY, self.youtube_id)
                print("Downloading...")
                YTHelper.download_specific_video(self, videos, video_resolution)
                os.chdir(WORKSPACE)
                print("Done!")
        else:
            print("Downloading...")
            YTHelper.prepare_place_for_download(VIDEO_DIRECTORY, self.youtube_id)
            YTHelper.download_specific_video(self, videos, DEFAULT_RESOLUTION)
            os.chdir(WORKSPACE)
            print("Done!")

    def download_audio(self, average_bitrate=None):
        """ Download the audio itself"""
        audios = self.youtube_video.streams.filter(only_audio=True)
        if average_bitrate is not None:
            average_bitrate = average_bitrate + 'kbps'

            if (not YTHelper.check_empty_list_of_candidates(audios)
                and YTHelper.check_bitrate_in_candidates(audios, average_bitrate)):
                print("Downloading...")
                YTHelper.prepare_place_for_download(AUDIO_DIRECTORY, self.youtube_id)
                audios.filter(abr=average_bitrate)[0] \
                      .download(
                          filename=self.get_video_title() +
                          f'_{average_bitrate}.mp3'
                      )
                os.chdir(WORKSPACE)
                print("Done!")
        else:
            highest_birate = str(YTHelper.get_highest_audio_quality(audios)) + 'kbps'
            print("Downloading...")
            YTHelper.prepare_place_for_download(AUDIO_DIRECTORY, self.youtube_id)
            audios.filter(abr=highest_birate)[0] \
                  .download(
                      filename=self.get_video_title() +
                      f'_{highest_birate}.mp3'
                  )
            os.chdir(WORKSPACE)
            print("Done!")

    def download_video_with_audio(self, video_resolution=None):
        """Download video with audio (if it's avaiable)"""
        videos = self.youtube_video.streams \
                                   .filter(
                                        progressive=True,
                                        resolution=video_resolution
                                    )
        if video_resolution is not None:
            if not YTHelper.check_empty_list_of_candidates(videos):
                YTHelper.prepare_place_for_download(VIDEO_AND_AUDIO_DIRECTORY, self.youtube_id)
                print("Downloading...")
                YTHelper.download_specific_video(self, videos, video_resolution)
                os.chdir(WORKSPACE)
                print("Done!")
        else:
            YTHelper.prepare_place_for_download(VIDEO_AND_AUDIO_DIRECTORY, self.youtube_id)
            print("Downloading...")
            videos.get_highest_resolution() \
                  .download(
                      filename=self.get_video_title() +
                      f'_{videos.get_highest_resolution().resolution}.{VIDEO_FORMAT}'
                  )
            os.chdir(WORKSPACE)
            print("Done!")

    def get_video_title(self):
        """Returns YT video title"""
        return self.youtube_video.title

    def get_video_duration(self):
        """Returns duration on YT video"""
        return str(datetime.timedelta(seconds=self.youtube_video.length))

