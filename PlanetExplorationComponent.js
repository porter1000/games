// PlanetExplorationComponent.js
import React from 'react';
import { useGame } from './GameContext';

const PlanetExplorationComponent = () => {
  const { currentPlanet } = useGame(); // Assume this includes the current location

  return (
    <div>
      <h3>Exploring {currentPlanet.name}</h3>
      <p>{currentPlanet.description}</p>
      <div>
        {currentPlanet.locations.map((location) => (
          <div key={location.name}>
            <h4>{location.name}</h4>
            <p>{location.description}</p>
            {/* Add buttons or interactions for specific location actions */}
          </div>
        ))}
      </div>
    </div>
  );
};

export default PlanetExplorationComponent;
