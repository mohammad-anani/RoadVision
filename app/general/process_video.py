import cv2
from general.handle_frame import handle_frame


def iterate_over_video_frames(video_path):
  """
  Runs the video path and handles each frame.
  """

  cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
  cv2.resizeWindow("Video", 1280, 720)

  video = cv2.VideoCapture(video_path)

  while True:
    success, frame = video.read()

    if not success:
      break

    handled_frame = handle_frame(frame)

    cv2.imshow("Video", handled_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
      break

  video.release()
  cv2.destroyAllWindows()