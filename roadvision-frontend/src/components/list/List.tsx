import type { DetectedCar } from "../../util/types";
import { EmptyList } from "./EmptyList";
import { ListItem } from "./listItem/ListItem";

export function List({ cars }: { cars: DetectedCar[]; }) {
  return <>
    {cars.length > 0 ? (
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {cars.map((car) => (
          <ListItem car={car} />
        ))}
      </div>
    ) : (
      <EmptyList />
    )}
  </>;
}



