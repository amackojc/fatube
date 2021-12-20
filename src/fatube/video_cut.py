from moviepy.editor import VideoFileClip


def cut_video(path_to_video, start_time, end_time):
    """ Returns the cut video """
    clip = VideoFileClip(path_to_video)
    clip = clip.subclip(start_time, end_time)
    clip.write_videofile(f'{path_to_video.replace(".mp4", "")}_cut.mp4')
