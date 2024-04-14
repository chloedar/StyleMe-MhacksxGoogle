import HomePage from './components/HomePage';
import './App.css'
import Typical from 'react-typical';
import React from 'react';
import Tabs from './Tabs'
import myImage from './arrowdown.png';
// import Typed from 'react-typed';

function App() {
  return (
    <div className='App'>
      <header className='App-header'>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia"></link>
        <img src='favicon.ico' alt="Logo"/>
        <h1> Hi, I'm styleMe </h1>
        <p> I'm your {' '}
          <Typical
            loop={Infinity}
            wrapper="b"
            steps={[
              'fashionista 👑 ',
              3500,
              'realest friend 😍 ',
              3500, 
              'biggest inspiration 🤩 ',
              3500,
              'Pinterest crush ❤️ ',
              3500,
              'AI stylist 🤖 ',
              3500,
            ]}
          />
        </p>
        {/* <br />
        <br />
        <h5> Scroll down to test it out! </h5>
        <h5> ⬇️ </h5>
        <img src={myImage} alt="down arrow" /> */}
      </header>
      <Tabs />
    </div>
  );
}

export default App;