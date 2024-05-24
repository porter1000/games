import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { GameProvider } from './GameContext';
import StartingScreen from './StartingScreen';
import CharacterCreation from './CharacterCreation';
import MainGame from './MainGame';
import Settings from './Settings';

const App = () => {
  return (
    <GameProvider>
      <Router>
        <div className="App">
          <Routes>
            <Route path="/" element={<StartingScreen />} />
            <Route path="/characterCreation" element={<CharacterCreation />} />
            <Route path="/mainGame" element={<MainGame />} />
            <Route path="/settings" element={<Settings />} />
            <Route path="*" element={<Navigate to="/" />} /> {/* Redirect unknown paths to home */}
          </Routes>
        </div>
      </Router>
    </GameProvider>
  );
};

export default App;
