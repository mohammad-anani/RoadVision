import type { DetectedCar } from "../../../../util/types";
import { Confidence } from "../Confidence";
import { CarInfoData } from "./CarInfoData";


export function CarInfo({ car }: { car: DetectedCar; }) {
  return (
    <div className="min-h-10">
      <p className="text-xs font-semibold tracking-wide text-primary">
        Vehicle Info
      </p>

      {car.carInfo ? (
        <div className="flex items-baseline justify-between gap-2">
          <CarInfoData carInfo={car.carInfo} />

          {car.carInfoConfidence !== null && (
            <Confidence value={car.carInfoConfidence} />
          )}
        </div>
      ) : (
        <div className="h-6" />
      )}
    </div>
  );
}
