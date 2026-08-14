export function ListLengthLabel({ listLength }: { listLength: number; }) {
  return <p className="ml-3 mt-1 text-sm text-muted">
    {listLength}{" "}
    {listLength === 1 ? "vehicle" : "vehicles"} detected
  </p>;
}
