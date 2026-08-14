from general.process_video import iterate_over_video_frames

VIDEO_PATH = "./input/RoadVideo.mp4"

def main():
  """
  Main entry of the app 
  """
  iterate_over_video_frames(VIDEO_PATH)

main()