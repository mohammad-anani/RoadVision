import type { FilterType, Setter } from "../../util/types";
import { CarInfoInput } from "./CarInfoInput";
import { FilterHeader } from "./FilterHeader";
import { FromDateInput } from "./FromDateInput";
import { PlateNumberInput } from "./PlateNumberInput";
import { ToDateInput } from "./ToDateInput";

export type UpdateFilter = (
  key: keyof FilterType,
  value: string
) => void;

export function Filter({
  filter,
  setFilter,
}: {
  filter: FilterType;
  setFilter: Setter<FilterType>;
}) {

  const updateFilter: UpdateFilter = (key, value) => {
    setFilter((previous) => ({
      ...previous,
      [key]: value,
    }));
  };

  return (
    <section className="mb-7 rounded-xl border border-background-darker bg-white p-5 shadow-sm">
      <FilterHeader />

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <FromDateInput
          filter={filter}
          updateFilter={updateFilter}
        />

        <ToDateInput
          filter={filter}
          updateFilter={updateFilter}
        />

        <CarInfoInput
          filter={filter}
          updateFilter={updateFilter}
        />

        <PlateNumberInput
          filter={filter}
          updateFilter={updateFilter}
        />
      </div>
    </section>
  );
}

