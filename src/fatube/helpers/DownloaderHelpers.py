import pathlib
import os

def prepare_directory(folder_name):
    pathlib.Path(f'{folder_name}').mkdir(
                                    parents=True,
                                    exist_ok=True
                                    )

def prepare_place_for_download(directory_output, youtube_id):

    prepare_directory(f'{youtube_id}/{directory_output}')
    os.chdir(f'{youtube_id}/{directory_output}')
    # prepare_directory(directory_output)
    # os.chdir(directory_output)

def get_highest_audio_quality(yt_audio):
    list_of_qualities = [int(audio.abr.replace("kbps", "")) for audio in yt_audio]
    highest = max(list_of_qualities)
    return highest

def check_empty_list_of_candidates(list_of_candidates):
    if not list_of_candidates:
        print("No candidates to download...")
        return True
    else:
        return False


def check_bitrate_in_candidates(yt_audio, candidate):
    list_of_candidates = [audio.abr for audio in yt_audio]
    if candidate in list_of_candidates:
        return True
    else:
        print("No candidates to download...")
        return False


def download_specific_video(self, yt_video, video_resolution):
    yt_video.filter(resolution=video_resolution)[0] \
          .download(
              filename=self.get_video_title() +
              f'_{video_resolution}.mp4'
              )

    
