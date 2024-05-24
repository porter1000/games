import React from 'react';
import { useGame } from './GameContext';
import './Sidebar.css'; // Import the CSS file

function Sidebar() {
  const { characterDetails, bits, age, startingPlanet, scale } = useGame();

  // Convert the scale coordinates into a color
  const getColorFromScale = (scale) => {
    // Assuming simple RGB color generation based on scale coordinates
    const red = Math.floor(scale.x * 255);
    const green = Math.floor(scale.y * 255);
    const blue = Math.floor(scale.z * 255);
    return `rgb(${red}, ${green}, ${blue})`;
  };

  // Get the color from the scale coordinates
  const scaleColor = getColorFromScale(scale);

  return (
    <div className="sidebar">
      <h2>Character Details</h2>
      <p>Name: {characterDetails.name}</p>
      <p>Age: {age}</p>
      <p>Species: {characterDetails.species}</p>
      <p>Planet: {startingPlanet}</p>
      <p>Bits: {bits}</p>
      <p>Scale: <span style={{ color: scaleColor }}>{scale.x}, {scale.y}, {scale.z}</span></p>
      <h2>Parental Influence</h2>
      <p>Mother: {characterDetails.parentalInfluence.mother}</p>
      <p>Father: {characterDetails.parentalInfluence.father}</p>
    </div>
  );
}

export default Sidebar;
