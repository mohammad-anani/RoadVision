import type { DetectedCar, FilterType } from "../util/types";

export default function useFilter(
  cars: DetectedCar[],
  filter: FilterType
) {
  return cars.filter((car) => {
    // From date
    if (
      filter.fromDate &&
      new Date(car.detectedAt) < new Date(filter.fromDate)
    ) {
      return false;
    }

    // To date
    if (
      filter.toDate &&
      new Date(car.detectedAt) > new Date(filter.toDate)
    ) {
      return false;
    }

    // Car info search
    if (
      filter.carInfoSearch &&
      !car.carInfo
        ?.toLowerCase()
        .includes(filter.carInfoSearch.toLowerCase())
    ) {
      return false;
    }

    // Plate number search
    if (
      filter.plateSearch &&
      !car.plateNumber
        ?.toLowerCase()
        .includes(filter.plateSearch.toLowerCase())
    ) {
      return false;
    }

    return true;
  });
}