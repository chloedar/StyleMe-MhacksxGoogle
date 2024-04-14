import HomePage from './components/HomePage';
import './App.css'
import Typical from 'react-typical';
import React from 'react';
import Tabs from './Tabs'
// import Typed from 'react-typed';

function App() {
  return (
    <div className='App'>
      <header className='App-header'>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia"></link>
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
      </header>
      Scroll down to test it out!
      <Tabs />
    </div>
  );
}

// const App = () => {
//   return (
//     <div>
//       <h1>
//         Welcome to{" "}
//         <Typed
//           strings={["My React App"]}
//           typeSpeed={100}
//           loop
//           backSpeed={20}
//           cursorChar=">"
//           showCursor={true}
//         />
//       </h1>
//     </div>
//   );
// };

export default App;

// function App() {
//   const [text, setText] = useState('');
//   const phrases = ["Hello, World!", "This is a typing animation.", "Feel free to customize it!"];

//   useEffect(() => {
//     const intervalId = setInterval(() => {
//       setText(phrases[Math.floor(Math.random() * phrases.length)]);
//     }, 2000); // Change the interval as needed

//     return () => clearInterval(intervalId);
//   }, [phrases]); // Runs once on component mount

//   return (
//     <div className="App">
//       <header className="App-header">
//         <h1>Welcome to StyleMe</h1>
//         <div className="typing-animation">
//           <span>{text}</span>
//           <span className="blink-caret"></span> {/* Blinking cursor */}
//         </div>
//       </header>
//       <div>
//         <HomePage/>
//       </div>
//     </div>
//   );
// }