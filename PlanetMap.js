// PlanetMap.js
import React from 'react';
import planets from './planetsData'; // Import your planet data

const PlanetMap = ({ onPlanetSelect }) => {
  return (
    <div className="planet-map">
      {planets.map((planet) => (
        <div
          key={planet.name}
          className="planet"
          style={{ left: `${planet.coordinates.x}px`, top: `${planet.coordinates.y}px` }} // Position based on coordinates
          onClick={() => onPlanetSelect(planet.name)}
        >
          {planet.name}
        </div>
      ))}
    </div>
  );
};

export default PlanetMap;
