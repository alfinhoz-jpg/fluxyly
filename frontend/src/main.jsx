import React from "react";
import reactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./index.css";
import Empresas from "./pages/Empresas";

reactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Empresas />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
