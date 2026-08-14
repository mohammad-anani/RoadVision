from car_inserter.prepare_request import prepare_request
import requests

API_URL = "https://localhost:7047/api/detected-cars"


def insert_cars(cars_to_insert):
  for car in cars_to_insert:
    insert_car(car)


def insert_car(car):
  form_data, files = prepare_request(car)

  print("Form data:")
  print(form_data)

  try:
    response = requests.post(
      API_URL,
      data=form_data,
      files=files,
      verify=False
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

  except requests.RequestException as e:
    print("Request failed:")
    print(e)


  return response.json()