import React from "react";
import { useEmpresas } from "../useEmpresas";

console.log("Empresas está carregando.");

function Empresas() {
  const { empresas, loading } = useEmpresas();

  if (loading) return <p>Carregando...</p>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Locais Disponíveis</h1>
      <ul className="space-y-2">
        {empresas.map((empresa) => (
          <li key={empresa.id} className="p-4 border rounded-lg shadow-md">
            <h2 className="text-xl font-semibold">{empresa.nome}</h2>
            <p>
              {empresa.tipo} - {empresa.endereco}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
}
export default Empresas;
