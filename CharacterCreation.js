import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useGame } from './GameContext';
import PlanetMap from './PlanetMap';
import planets from './planetsData'; // Import the planets array
import './PlanetMap.css';
import './CharacterCreation.css';

function CharacterCreation() {
  const { finishCharacterCreation, updateStartingPlanet } = useGame();
  const [characterDetails, setCharacterDetails] = useState({
    name: '',
    age: 0,
    species: '',
    startingPlanet: '',
    parentalInfluence: { mother: '', father: '' },
    archetype: '',
    profession: '',
  });

  useEffect(() => {
    // Generate initial parental influence
    const influences = ['supportive', 'average', 'neglectful', 'absent'];
    const motherInfluence = influences[Math.floor(Math.random() * influences.length)];
    const fatherInfluence = influences[Math.floor(Math.random() * influences.length)];

    setCharacterDetails(currentDetails => ({
      ...currentDetails,
      parentalInfluence: {
        mother: motherInfluence,
        father: fatherInfluence,
      },
    }));
  }, []);

  const handlePlanetSelect = (planetName) => {
    const selectedPlanet = planets.find(planet => planet.name === planetName);
    if (selectedPlanet) {
      setCharacterDetails({
        ...characterDetails,
        startingPlanet: selectedPlanet.name,
        species: getSpeciesForPlanet(selectedPlanet.name),
      });
      // Update the starting planet using the updateStartingPlanet function
      updateStartingPlanet(selectedPlanet.name);
    }
  };

  const navigate = useNavigate();

  const handleFinishCreation = () => {
    finishCharacterCreation(characterDetails);
    navigate('/mainGame');
  };

  const getSpeciesForPlanet = (planetName) => {
    switch (planetName) {
      case 'So-Hyu':
        return 'Nomads';
      case 'Qwari':
        return 'Aquans';
      case 'Aurlis':
        return 'Venturmans';
      case 'Vantera':
        return 'Urbanites';
      case 'Larabu':
        return 'Highlanders';
      default:
        return 'Standard Humans';
    }
  };

  return (
    <form className="character-creation-form" onSubmit={(e) => e.preventDefault()}>
      <div>
        <label htmlFor="name">Name:</label>
        <input
          id="name"
          name="name"
          value={characterDetails.name}
          onChange={(e) => setCharacterDetails({ ...characterDetails, name: e.target.value })}
          required
        />
      </div>

      <div>
        <label>Starting Planet:</label>
        <PlanetMap onPlanetSelect={handlePlanetSelect} />
        {characterDetails.startingPlanet && (
          <div>
            <p>Selected Planet: {characterDetails.startingPlanet}</p>
            <p>Description: {planets.find(planet => planet.name === characterDetails.startingPlanet)?.description}</p>
            <p>Species: {characterDetails.species}</p>
          </div>
        )}
      </div>

      <div>
        <p>Mother's Influence: {characterDetails.parentalInfluence.mother}</p>
        <p>Father's Influence: {characterDetails.parentalInfluence.father}</p>
      </div>

      <button type="button" onClick={handleFinishCreation}>Finish</button>
    </form>
  );
}

export default CharacterCreation;
