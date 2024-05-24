import React, { createContext, useContext, useState } from 'react';

const GameContext = createContext();

export const GameProvider = ({ children }) => {
  const [gameStage, setGameStage] = useState('characterCreation');
  const [characterDetails, setCharacterDetails] = useState({
    name: '',
    age: 0,
    startingPlanet: '',
    parentalInfluence: { mother: '', father: '' },
    archetype: '',
    profession: '',
  });
  const [bits, setBits] = useState(0);
  const [age, setAge] = useState(0);
  const [startingPlanet, setStartingPlanet] = useState('');
  const [scale, setScale] = useState({ x: 0, y: 0, z: 0 }); // Updated to represent coordinates in a 3D space
  const [ownedAssets, setOwnedAssets] = useState([]);

  const resetGameState = () => {
    setGameStage('characterCreation');
    setCharacterDetails({
      name: '',
      age: 0,
      startingPlanet: '',
      parentalInfluence: { mother: '', father: '' },
      archetype: '',
      profession: '',
    });
    setBits(0);
    setAge(0);
    setStartingPlanet('');
    setScale({ x: 0, y: 0, z: 0 }); // Reset the scale to zero coordinates
    setOwnedAssets([]);
    localStorage.removeItem('gameState'); // Clear game state from localStorage
  };

  const startNewGame = () => {
    resetGameState(); // Call resetGameState to ensure a clean start
    // Additional logic for starting a new game can be added here
  };

  // Define the finishCharacterCreation function
  const finishCharacterCreation = (details) => {
    setCharacterDetails(details); // Assume `details` is an object containing character details
    setGameStage('mainGame'); // Move the game stage to mainGame or another appropriate value
    // Potentially update other state values or perform additional setup here
  };

  return (
    <GameContext.Provider value={{
      gameStage,
      characterDetails,
      setCharacterDetails,
      bits,
      updateBits: (amount) => setBits(bits + amount),
      age,
      updateAge: setAge,
      startingPlanet,
      updateStartingPlanet: setStartingPlanet,
      scale,
      setScale,
      updateScale: setScale,
      ownedAssets,
      resetGameState,
      startNewGame,
      finishCharacterCreation, // Make finishCharacterCreation available in the context
    }}>
      {children}
    </GameContext.Provider>
  );
};

export const useGame = () => useContext(GameContext);
