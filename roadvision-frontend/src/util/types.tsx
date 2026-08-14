import type { Dispatch, SetStateAction } from "react";


export type DetectedCar = {
  id: number;
  detectedAt: string;
  carInfo: string | null;
  carInfoConfidence: number | null;
  plateNumber: string | null;
  plateNumberConfidence: number | null;
  imagePath: string | null;
};

export type Setter<T> = Dispatch<SetStateAction<T>>;

export type FilterType = {
  fromDate?: string,
  toDate?: string,
  carInfoSearch?: string,
  plateSearch?: string

}