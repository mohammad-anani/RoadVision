import type { MouseEventHandler } from "react";

export function RefreshButton({ onClick }: { onClick: MouseEventHandler<HTMLButtonElement> }) {
  return <button
    type="button"
    onClick={onClick}
    className="rounded-lg border border-white/30 bg-white px-4 py-2 text-sm font-semibold text-primary shadow-sm hover:bg-primary-light/20! hover:border-white! hover:text-white!"
  >
    Refresh
  </button>;
}
