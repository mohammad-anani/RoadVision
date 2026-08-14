export function Confidence({ value }: { value: number; }) {

  const percentage = value * 100
  return (
    <span className="shrink-0 text-xs font-bold text-primary">
      {percentage.toFixed()}%
    </span>
  );
}
