// Achievements.js
import React, { useEffect, useState } from 'react';
import Achievement from './Achievement';

const Achievements = () => {
  const [achievements, setAchievements] = useState([]);

  useEffect(() => {
    // Load achievements from local storage when component mounts
    const savedAchievements = JSON.parse(localStorage.getItem('achievements')) || [];
    setAchievements(savedAchievements);
  }, []);

  const saveAchievements = (updatedAchievements) => {
    // Save achievements to local storage
    localStorage.setItem('achievements', JSON.stringify(updatedAchievements));
    setAchievements(updatedAchievements);
  };

  // eslint-disable-next-line
  const unlockAchievement = (achievementName) => {
    // Check if the achievement is already unlocked
    const updatedAchievements = achievements.map((achievement) => {
      if (achievement.name === achievementName && !achievement.unlocked) {
        return { ...achievement, unlocked: true };
      }
      return achievement;
    });

    // Save updated achievements to local storage
    saveAchievements(updatedAchievements);
  };

  // eslint-disable-next-line
  const addProgressToAchievement = (achievementName, amount) => {
    // Increase progress of the achievement by the specified amount
    const updatedAchievements = achievements.map((achievement) => {
      if (achievement.name === achievementName && !achievement.unlocked) {
        return { ...achievement, progress: achievement.progress + amount };
      }
      return achievement;
    });

    // Save updated achievements to local storage
    saveAchievements(updatedAchievements);
  };

  return (
    <div className="achievements">
      
      {achievements.map((achievement) => (
        <Achievement key={achievement.name} achievement={achievement} />
      ))}
    </div>
  );
};

export default Achievements;
