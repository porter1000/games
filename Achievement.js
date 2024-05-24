// Achievement.js
import React from 'react';

const Achievement = ({ achievement }) => {
  const { name, description, progress, unlocked } = achievement;

  return (
    <div className={`achievement ${unlocked ? 'unlocked' : 'locked'}`}>
      <h3>{name}</h3>
      <p>{description}</p>
      <div className="progress">{unlocked ? `Progress: ${progress}` : 'Locked'}</div>
    </div>
  );
};

export default Achievement;
