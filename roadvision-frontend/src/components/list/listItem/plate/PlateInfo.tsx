import type { DetectedCar } from "../../../../util/types";
import { Confidence } from "../Confidence";
import { PlateData } from "./PlateData";

export function PlateInfo({ car }: { car: DetectedCar; }) {
  return (
    <div className="min-h-10">
      <p className="text-xs font-semibold  tracking-wide text-primary">
        Plate
      </p>

      {car.plateNumber ? (
        <div className="flex items-baseline justify-between gap-2">
          <PlateData plateNumber={car.plateNumber} />

          {car.plateNumberConfidence !== null && (
            <Confidence value={car.plateNumberConfidence} />
          )}
        </div>
      ) : (
        <div className="h-6" />
      )}
    </div>
  );
}
