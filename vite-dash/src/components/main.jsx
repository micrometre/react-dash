import "tailwindcss/tailwind.css";
import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter as Router, Route, BrowserRouter } from "react-router-dom";
import App from './App.jsx'
import './index.css'
import DashboardLayout from "./dashboard/Layout.jsx"


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
          <App />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)
