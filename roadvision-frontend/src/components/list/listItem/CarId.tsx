export function CarId({ id }: { id: number; }) {
  return (
    <div className="absolute left-3 top-3 rounded-md bg-primary px-2 py-1 text-[10px] font-bold uppercase tracking-wider text-white shadow-sm">
      #{id}
    </div>
  );
}
