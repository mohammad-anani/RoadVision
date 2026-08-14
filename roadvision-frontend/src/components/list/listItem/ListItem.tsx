import type { DetectedCar } from "../../../util/types";
import { CarId } from "./CarId";
import { CarImage } from "./CarImage";
import { CarInfo } from "./carInfo/CarInfo";
import { DetectedInfo } from "./DetectedInfo";
import { PlateInfo } from "./plate/PlateInfo";

export function ListItem({ car }: { car: DetectedCar }) {
  return (
    <article
      key={car.id}
      className="group overflow-hidden rounded-xl border border-background-darker bg-white shadow-sm hover:-translate-y-1 hover:border-primary hover:shadow-lg"
    >
      <div className="relative flex h-56 items-center justify-center border-b-2 border-background-darker bg-background-dark p-3">
        <CarId id={car.id} />

        <CarImage imagePath={car.imagePath ?? undefined} />
      </div>

      <div className="space-y-3 p-4">
        <CarInfo car={car} />

        <PlateInfo car={car} />

        <DetectedInfo detectedAt={car.detectedAt} />
      </div>
    </article>
  );
}


