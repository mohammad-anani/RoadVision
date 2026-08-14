import type { FilterType } from "../../util/types";
import type { UpdateFilter } from "./Filter";

export function CarInfoInput({
  filter, updateFilter,
}: {
  filter: FilterType;
  updateFilter: UpdateFilter;
}) {
  return (
    <div>
      <label
        htmlFor="carInfo"
        className="mb-1.5 block text-sm font-medium text-foreground"
      >
        Car info
      </label>

      <input
        id="carInfo"
        type="text"
        placeholder="e.g. Toyota"
        value={filter.carInfoSearch ?? ""}
        onChange={(e) => updateFilter("carInfoSearch", e.target.value)}
        className="w-full rounded-lg border border-background-darker bg-background px-3 py-2.5 text-sm text-foreground placeholder:text-muted outline-none focus:border-primary focus:bg-white focus:ring-2 focus:ring-primary-light/30" />
    </div>
  );
}
