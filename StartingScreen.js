import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useGame } from './GameContext'; // Import the useGame hook
import './StartingScreen.css'; // Import CSS file for styling

const StartingScreen = () => {
  const navigate = useNavigate(); // Initialize useNavigate hook
  const { startNewGame } = useGame(); // Destructure startNewGame from context

  const handleNewGame = () => {
    console.log("New Game button clicked");
    startNewGame(); // Use startNewGame from the context to reset and start a new game
    navigate('/characterCreation'); // Redirect to the characterCreation route
  };

  const handleLoadGame = () => {
    console.log("Load Game button clicked");
    // Implement game loading logic here, possibly involving context
    // For now, this is a placeholder for your onLoadGame functionality
    // navigate('/mainGame'); // Example redirect, adjust based on your load game implementation
  };

  const handleSettings = () => {
    console.log("Settings button clicked");
    navigate('/settings'); // Redirect to the settings route
  };

  return (
    <div className="starting-screen-container">
      <div className="header">
        <h1 className="title">Welcome to the Space Adventure</h1>
        <p className="subtitle">Embark on a journey across the cosmos!</p>
      </div>
      <div className="button-container">
        <button className="start-button" onClick={handleNewGame}>Start New Game</button>
        <button className="load-button" onClick={handleLoadGame}>Load Saved Game</button>
        <button className="settings-button" onClick={handleSettings}>Settings</button>
      </div>
      <div className="background-stars" />
    </div>
  );
};

export default StartingScreen;
