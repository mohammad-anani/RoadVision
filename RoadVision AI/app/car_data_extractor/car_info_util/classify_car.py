import torch
import timm
import csv
from PIL import Image
from torchvision import transforms


# Load model
checkpoint = torch.load("models/vehicle_classifier.pth", map_location="cpu")

car_classifier = timm.create_model(
  "efficientnet_b4",
  pretrained=False,
  num_classes=8949
)
car_classifier.load_state_dict(checkpoint["model_state"])
car_classifier.eval()

transform = transforms.Compose([
  transforms.Resize((380, 380)),
  transforms.ToTensor(),
  transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
  ),
])


# This process is based on the model worflow documented by its author
def classify_car(car_image):
  """
  Returns predicted info about the car(model, make, year)
  """

  image = Image.fromarray(car_image).convert("RGB")

  input_tensor = transform(image).unsqueeze(0)

  with torch.no_grad():
    logits = car_classifier(input_tensor)
    probabilities = torch.softmax(logits, dim=1)

  best_prob, best_index = torch.max(probabilities[0], dim=0)

  confidence = float(best_prob.item())

  return get_index_info(best_index.item()), confidence


def get_index_info(index):

  if index is None:
    return None

  with open("models/class_mapping.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
      if int(row["global_class_id"]) == index:
        return row

  return None



# ## Testing
# import numpy as np

# image = Image.open("input/car_image_test2.png").convert("RGB")
# img_array = np.array(image)

# print(classify_car(img_array))