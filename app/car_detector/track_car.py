import time
import cv2

def update_tracked_cars(result,tracked_cars, frame):

  if result.boxes.id is None:
    return tracked_cars

  track_ids = result.boxes.id.int().cpu().tolist()
  boxes = result.boxes.xyxy.int().cpu().tolist()

  # Iterate over each parallel id and box
  for track_id, box in zip(track_ids,boxes):

    x1, y1, x2, y2 = validate_box(box)

    box_area=calculate_box_area(x1,y1,x2,y2)

    if track_id not in tracked_cars:
      insert_car_into_tracked_cars(tracked_cars,track_id,box_area,(x1,y1,x2,y2))
    else:
      compare_and_update_tracked_car(tracked_cars,track_id,box_area,(x1,y1,x2,y2))


def validate_box(box):
  """
  Ensure box coordinates are within frame bound. Returns validated box coordinates
  """

  x1, y1, x2, y2 = box

  x1 = max(0, x1)
  y1 = max(0, y1)
  x2 = min(frame.shape[1], x2)
  y2 = min(frame.shape[0], y2)

  return x1,y1,x2,y2


def calculate_box_area(x1,y1,x2,y2):
  box_width = x2 - x1
  box_height = y2 - y1
  box_area = box_width * box_height

  return box_area


def insert_car_into_tracked_cars(tracked_cars,track_id,box_area,best_box):
  current_time = time.monotonic()

  tracked_cars[track_id] = {
  "track_id": track_id,
  "best_box_area": box_area,
  "best_box": best_box,
  "last_seen": current_time
  }


def compare_and_update_tracked_car(tracked_cars, track_id,box_area,best_box):
  """
  Update the tracked car to have the largest box area
  """

  current_time = time.monotonic()

  car = tracked_cars[track_id]
  car["last_seen"] = current_time

  if box_area > car["best_box_area"]:
    car["best_box_area"] = box_area
    car["best_box"]=best_box