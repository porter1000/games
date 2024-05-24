// Settings.js
import React from 'react';
import { Link } from 'react-router-dom';
import Achievements from './Achievements'; // Import the Achievements component
import './Settings.css'; // Import CSS file for styling

const Settings = () => {
  return (
    <div className="settings-container">
      <h2>Settings</h2>
      {/* Add your settings options here */}
      <Achievements /> {/* Include the Achievements component */}
      <Link to="/" className="back-button">Back to Start Screen</Link>
    </div>
  );
};

export default Settings;
