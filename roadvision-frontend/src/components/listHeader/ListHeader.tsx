import { ListLengthLabel } from "./ListLengthLabel";
import { Title } from "./Title";

export function ListHeader({ listLength }: { listLength: number; }) {
  return <div className="mb-5 flex items-end justify-between">
    <div>
      <Title />
      <ListLengthLabel listLength={listLength} />
    </div>
  </div>;
}



