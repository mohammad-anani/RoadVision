import { useEffect, useState } from "react";
import type { DetectedCar } from "../util/types";
import { API_URL } from "../util/URL";

export default function useCars() {
  const [cars, setCars] = useState<DetectedCar[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function fetchCars() {
    try {

      setLoading(true);
      setError(null);

      const response = await fetch(
        `${API_URL}api/detected-cars`
      );

      if (!response.ok) {
        throw new Error("Failed to fetch detected cars");
      }

      const data: DetectedCar[] = await response.json();

      setCars(data);
    } catch (error) {
      setError(
        error instanceof Error
          ? error.message
          : "An unknown error occurred"
      );
    } finally {
      setLoading(false);
    }
  };


  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    fetchCars();
  }, []);

  return {
    cars,
    loading,
    error,
    refresh: fetchCars
  };
}