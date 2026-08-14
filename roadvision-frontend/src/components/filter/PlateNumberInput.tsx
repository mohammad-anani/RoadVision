import type { FilterType } from "../util/types";
import type { UpdateFilter } from "./Filter";

export function PlateNumberInput({
  filter, updateFilter,
}: {
  filter: FilterType;
  updateFilter: UpdateFilter;
}) {
  return (
    <div>
      <label
        htmlFor="plate"
        className="mb-1.5 block text-sm font-medium text-foreground"
      >
        Plate number
      </label>

      <input
        id="plate"
        type="text"
        placeholder="e.g. 123456"
        value={filter.plateSearch ?? ""}
        onChange={(e) => updateFilter("plateSearch", e.target.value)}
        className="w-full rounded-lg border border-background-darker bg-background px-3 py-2.5 text-sm text-foreground placeholder:text-muted outline-none focus:border-primary focus:bg-white focus:ring-2 focus:ring-primary-light/30" />
    </div>
  );
}
