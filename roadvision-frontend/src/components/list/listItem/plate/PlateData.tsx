export function PlateData({ plateNumber }: { plateNumber: string; }) {
  return (
    <p className="font-semibold tracking-wide text-foreground">
      {plateNumber}
    </p>
  );
}
