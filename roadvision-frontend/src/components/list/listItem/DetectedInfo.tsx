import { formatDate } from "../../../util/formatDate";

export function DetectedInfo({ detectedAt }: { detectedAt: string; }) {
  return (
    <div className="border-t border-background-darker pt-3">
      <p className="text-xs font-semibold tracking-wide text-primary">
        Detected At
      </p>

      <p className="mt-0.5 text-sm font-medium text-muted">
        {formatDate(detectedAt)}
      </p>
    </div>
  );
}
