import type { FilterType } from "../util/types";
import type { UpdateFilter } from "./Filter";

export function ToDateInput({
  filter, updateFilter,
}: {
  filter: FilterType;
  updateFilter: UpdateFilter;
}) {
  return (
    <div>
      <label
        htmlFor="toDate"
        className="mb-1.5 block text-sm font-medium text-foreground"
      >
        To
      </label>

      <input
        id="toDate"
        type="datetime-local"
        value={filter.toDate ?? ""}
        onChange={(e) => updateFilter("toDate", e.target.value)}
        className="w-full rounded-lg border border-background-darker bg-background px-3 py-2.5 text-sm text-foreground outline-none focus:border-primary focus:bg-white focus:ring-2 focus:ring-primary-light/30" />
    </div>
  );
}
