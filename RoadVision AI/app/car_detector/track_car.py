import time
from datetime import datetime
from zoneinfo import ZoneInfo

def update_tracked_cars(result, tracked_cars, frame):

  if result.boxes.id is None:
    print("No Ids found to track")
    return

  track_ids = result.boxes.id.int().cpu().tolist()
  boxes = result.boxes.xyxy.int().cpu().tolist()

  # Iterate over each parallel id and box
  for track_id, box in zip(track_ids, boxes):

    x1, y1, x2, y2 = validate_box(box, frame)

    box_area = calculate_box_area(x1, y1, x2, y2)

    if box_area <= 0:
      print("Car #"+str(track_id)+"Invalid Box area")
      continue

    if track_id not in tracked_cars:
      insert_car_into_tracked_cars(tracked_cars, track_id, box_area, (x1, y1, x2, y2), frame)
    else:
      compare_and_update_tracked_car(tracked_cars, track_id, box_area, (x1, y1, x2, y2), frame)


def validate_box(box, frame):
  """
  Ensure box coordinates are within frame bound. Returns validated box coordinates
  """

  x1, y1, x2, y2 = box

  x1 = max(0, x1)
  y1 = max(0, y1)
  x2 = min(frame.shape[1], x2)
  y2 = min(frame.shape[0], y2)

  return x1, y1, x2, y2


def calculate_box_area(x1, y1, x2, y2):
  box_width = x2 - x1
  box_height = y2 - y1
  box_area = box_width * box_height

  return box_area


def crop_car_image(frame, box):
  x1, y1, x2, y2 = box
  return frame[y1:y2, x1:x2].copy()


def insert_car_into_tracked_cars(tracked_cars, track_id, box_area, best_box, frame):
  current_time = datetime.now(ZoneInfo("Asia/Beirut"))

  tracked_cars[track_id] = {
    "track_id": track_id,
    "best_box_area": box_area,
    "best_box": best_box,
    "best_image": crop_car_image(frame, best_box),
    "best_time": current_time,
    "last_seen": current_time
  }


def compare_and_update_tracked_car(tracked_cars, track_id, box_area, best_box, frame):
  """
  Update the tracked car to have the largest box area
  """

  current_time = datetime.now(ZoneInfo("Asia/Beirut"))

  car = tracked_cars[track_id]
  car["last_seen"] = current_time

  if box_area > car["best_box_area"]:
    car["best_box_area"] = box_area
    car["best_box"] = best_box
    car["best_time"]= current_time
    car["best_image"] = crop_car_image(frame, best_box)