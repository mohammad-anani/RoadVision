import { API_URL } from "../../../util/URL";

export function CarImage({ imagePath }: { imagePath?: string; }) {
  return (
    <>
      {imagePath ? (
        <img
          src={`${API_URL}${imagePath}`}
          alt="Detected car"
          className="h-full w-full object-contain" />
      ) : (
        <div className="flex h-full w-full items-center justify-center text-sm text-muted">
          No image
        </div>
      )}
    </>
  );
}
