import React, { useState, useEffect } from 'react';
import './TypingAnimation.css'; // Import CSS file for styling

const TypingAnimation = () => {
  const [text, setText] = useState('');
  const phrases = ["Hello, World!", "This is a typing animation.", "Feel free to customize it!"];

  useEffect(() => {
    const intervalId = setInterval(() => {
      setText(phrases[Math.floor(Math.random() * phrases.length)]);
    }, 2000); // Change the interval as needed

    return () => clearInterval(intervalId);
  }, []); // Runs once on component mount

  return (
    <div className="typing-animation">
      <span>{text}</span>
      <span className="blink-caret"></span> {/* Blinking cursor */}
    </div>
  );
}

export default TypingAnimation;