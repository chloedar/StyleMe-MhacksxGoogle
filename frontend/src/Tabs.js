import { useState } from "react";
import "./App.css";
import React from "react";
import WardrobeSearch from './components/WardrobeSearch'
import GoShopping from './components/GoShopping'

const Tabs = () => {
  const [activeTab, setActiveTab] = useState("tab1");

  const handleTab1 = () => {
    // update the state to tab1
    setActiveTab("tab1");
  };
  const handleTab2 = () => {
    // update the state to tab2
    setActiveTab("tab2");
  };

  return (
    <div className="Tabs">
      {/* Tab nav */}
      <ul className="nav">
        <li className={activeTab === "tab1" ? "active" : ""} onClick={handleTab1}>Search your wardrobe</li>
        <li className={activeTab === "tab2" ? "active" : ""} onClick={handleTab2}>Go shopping</li>
      </ul>
      <div className="outlet">
        {activeTab === "tab1" ? <WardrobeSearch /> : <GoShopping />}
      </div>
    </div>
  );
};
export default Tabs;