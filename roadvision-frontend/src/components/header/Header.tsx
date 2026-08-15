import type { MouseEventHandler } from "react";
import { RefreshButton } from "./RefreshButton";
import { Subtitle } from "./Subtitle";
import { Title } from "./Title";


export function Header({ onRefreshClick }: { onRefreshClick: MouseEventHandler<HTMLButtonElement> }) {
  return <header className="border-b border-primary bg-primary shadow-md rounded-t-none!">
    <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
      <div>
        <Title />
        <Subtitle />
      </div>
      <RefreshButton onClick={onRefreshClick} />
    </div>
  </header>;
}



