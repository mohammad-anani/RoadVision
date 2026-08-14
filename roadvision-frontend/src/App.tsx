import { useState } from "react";
import { Filter } from "./components/filter/Filter";
import { Header } from "./components/header/Header";
import { List } from "./components/list/List";
import { ListHeader } from "./components/listHeader/ListHeader";
import useCars from "./hooks/useCars";
import useFilter from "./hooks/useFilter";
import type { FilterType } from "./util/types";

export const API_URL = "https://localhost:7047";

function App() {
  const [filter, setFilter] = useState<FilterType>({});

  const {
    cars,
    loading,
    error,
  } = useCars();

  const filteredCars = useFilter(cars, filter)

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header />

      <main className="mx-auto max-w-7xl px-4 py-7 sm:px-6 lg:px-8">
        <Filter
          filter={filter}
          setFilter={setFilter}
        />

        <ListHeader listLength={cars.length} />

        <FetchingStatesHandlers loading={loading} error={error} />

        {!loading && !error && (
          <List cars={filteredCars} />
        )}
      </main>
    </div>
  );
}

export default App;

function FetchingStatesHandlers({ loading, error }: { loading: boolean, error: string | null }) {
  return <>
    {loading && (
      <div className="py-10 text-center text-muted">
        Loading detected vehicles...
      </div>
    )}

    {error && (
      <div className="rounded-lg border border-red-300 bg-red-50 p-4 text-red-700">
        {error}
      </div>
    )}
  </>;
}
