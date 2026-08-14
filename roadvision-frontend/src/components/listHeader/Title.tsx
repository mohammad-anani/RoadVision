export function Title() {
  return <div className="flex items-center gap-2">

    {/*Vertical UI Line */}
    <div className="h-5 w-1 rounded-full bg-primary" />

    <h2 className="text-2xl font-bold text-foreground">
      Detected Cars
    </h2>
  </div>;
}
