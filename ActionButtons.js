// ActionButtons.js
import React from 'react';
import './ActionButtons.css'; // Import the CSS file for styling

function ActionButtons({ onPassWeek, onAssets, onOccupation, onRelationships, onActivities }) {
  return (
    <div className="action-buttons-container">
      <button className="action-button" onClick={onAssets}>Assets</button>
      <button className="action-button" onClick={onOccupation}>Occupation</button>
      {/* Connect the onAgeButtonClick function to the Age button click event */}
      <button className="action-button" onClick={onPassWeek}>Age</button>
      <button className="action-button" onClick={onRelationships}>Relationships</button>
      <button className="action-button" onClick={onActivities}>Activities</button>
    </div>
  );
}

export default ActionButtons;
