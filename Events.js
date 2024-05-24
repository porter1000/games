// MainGame.js

import React, { useState, useEffect, useRef } from 'react';
import { useGame } from './GameContext';
import Sidebar from './Sidebar';
import Events from './Events';
import ActionButtons from './ActionButtons';
import AssetsPanel from './components/AssetsPanel';

import './MainGame.css';

const MainGame = () => {
  const { characterDetails, bits, age, updateAge } = useGame();
  const [currentWeek, setCurrentWeek] = useState(1);
  const [showAssetsPanel, setShowAssetsPanel] = useState(false);
  const hasMounted = useRef(false);

  // Load the saved game state from localStorage on component mount
  useEffect(() => {
    if (!hasMounted.current) {
      const savedGameState = JSON.parse(localStorage.getItem('gameState'));
      if (savedGameState) {
        setCurrentWeek(savedGameState.currentWeek);
        if (savedGameState.age !== age) {
          updateAge(savedGameState.age);
        }
        setShowAssetsPanel(savedGameState.showAssetsPanel || false);
      }
      hasMounted.current = true;
    }
  }, [age, updateAge]);

  // Save the game state to localStorage whenever it changes
  useEffect(() => {
    const gameState = {
      currentWeek,
      age,
      showAssetsPanel,
    };
    localStorage.setItem('gameState', JSON.stringify(gameState));
  }, [currentWeek, age, showAssetsPanel]);

  // Function to handle passing a week
  const handlePassWeek = () => {
    setCurrentWeek(prevWeek => prevWeek + 1); // Increment currentWeek
    updateAge(age + 1); // Increment age
  };

  return (
    <div className="main-game-container">
      <Events /> {/* Events component will handle events on "Age" button click */}
      <ActionButtons onPassWeek={handlePassWeek} />
      {showAssetsPanel && <AssetsPanel />}
      <Sidebar characterDetails={characterDetails} bits={bits} />
    </div>
  );
};

export default MainGame;
