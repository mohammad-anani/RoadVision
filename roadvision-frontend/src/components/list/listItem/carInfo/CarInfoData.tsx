export function CarInfoData({ carInfo }: { carInfo: string; }) {
  return (
    <p className="truncate font-semibold text-foreground">
      {carInfo}
    </p>
  );
}
