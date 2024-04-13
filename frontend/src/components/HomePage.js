import React from 'react';
import { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import GoShopping from './GoShopping.js'
import WardrobeSearch from './WardrobeSearch.js'
// import "bootstrap/dist/css/bootstrap.min.css";
// import { FileUpload } from 'primereact/fileupload';   
// import "./App.css";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

const HomePage = () => {
  return (
    <div>
      Hello
      <Router>
          <Routes>
              <Route path="/GoShopping" element={<GoShopping />} />
              <Route
                  path="/WardrobeSearch"
                  element={<WardrobeSearch />}
              />
          </Routes>
      </Router>
    </div>
);
}

export default HomePage;