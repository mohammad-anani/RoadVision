# from get_plate_detection_model import get_model
from car_data_extractor.plate_number_util.get_plate_detection_model import get_model


plate_detector = get_model()

MIN_CONFIDENCE = 0.5

def detect_plate(car_image):
  """
  Returns the box of the first detected plate
  """

  results = plate_detector(car_image, conf=MIN_CONFIDENCE, verbose=False)

  for result in results:
    if result.boxes is None or len(result.boxes) == 0:
      return None

    box = result.boxes[0]
    return box


## Testing
# import numpy as np
# from PIL import Image

# image = Image.open("input/car_image_test.png").convert("RGB")
# img_array = np.array(image)

# box = detect_plate(img_array)

# if box is not None:
#   x1, y1, x2, y2 = box.xyxy[0].tolist()
#   x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

#   cropped = image.crop((x1, y1, x2, y2))
#   cropped.save("input/detected_plate_test.png")
#   print(f"Saved plate crop: ({x1}, {y1}, {x2}, {y2})")
# else:
#   print("No plate detected")