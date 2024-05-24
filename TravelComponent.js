// TravelComponent.js
import React from 'react';
import { useGame } from './GameContext'; // Assuming this holds your game state

const TravelComponent = () => {
  const { planets, setCurrentPlanet } = useGame(); // Ensure your context provides these

  const handleTravel = (planetKey) => {
    setCurrentPlanet(planets[planetKey]);
    // Additional logic for traveling, such as updating game state or triggering events
  };

  return (
    <div>
      <h2>Travel to a New Planet</h2>
      {Object.keys(planets).map((key) => (
        <button key={key} onClick={() => handleTravel(key)}>
          Travel to {planets[key].name}
        </button>
      ))}
    </div>
  );
};

export default TravelComponent;

