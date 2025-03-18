import { useState, useEffect } from "react";
import api from "./services/api";

export function useEmpresas() {
  const [empresas, setEmpresas] = useState([]);
  const [loading, setLoading] = useState([]);

  useEffect(() => {
    api
      .get("empresas/")
      .then((response) => {
        setEmpresas(response.data);
      })
      .catch((error) => {
        console.error("Erro ao buscar o local:", error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return { empresas, loading };
}
