import React from 'react';
import { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
// import "bootstrap/dist/css/bootstrap.min.css";
// import { FileUpload } from 'primereact/fileupload';   
// import "./App.css";     

const GoShopping = () => {
  const backgroundColor = "#f1d4ed";
  const otherBackgroundColor = "#daf1d4";
  const [query, setQuery] = useState("");
  const [file, setFile] = useState();
  const [sustainableBool, setSustainableBool] = useState(true);

  const toggleText = () => {
    setSustainableBool(!sustainableBool);
  };

  function handleChange(e) {
      console.log(e.target.files);
      setFile(URL.createObjectURL(e.target.files[0]));
  }

  function handleQueryUpdate(e) {
    setQuery(e.target.value);
  }

  useEffect(() => {
    document.title = "StyleMe";
  }, []);

  if (sustainableBool) {
    return (
      <div style={{ backgroundColor: otherBackgroundColor }}>
        <title>
          StyleMe
        </title>
        <body>
        <div>
          <header>
            <h1>Welcome to StyleMe</h1>
          </header>
          <h1>
            Build a brand new outfit!
          </h1>
          <div>
          <h2>
            <p>Type in the style you're looking for to receive an outfit suggestion curated from SUSTAINABLE fashion websites online.</p>
            <p>You can also provide a video link as a style reference.</p>
          </h2>
          </div>
          <form>
            <input
              type="text"
              value={query}
              onChange={handleQueryUpdate}
            >
            </input>
            <div className="App">
              <h2>Upload photos from your wardrobe:</h2>
              <input type="file" onChange={handleChange} multiple="multiple"/>
              <img src={file}  width="200" alt=""/>
            </div>
          </form>
          <div>
            <Button variant="contained" color="primary" onClick={toggleText}>
              <h3>In Sustainable Mode</h3>
            </Button>
          </div>
        </div>
        </body>
      </div>
    );
  }
  return (
    <div style={{ backgroundColor: backgroundColor }}>
      <title>
        StyleMe
      </title>
      <body>
      <div>
        <header>
          <h1>Welcome to StyleMe</h1>
        </header>
        <h1>
          Build a brand new outfit!
        </h1>
        <div>
        <h2>
            <p>Type in the style you're looking for to receive an outfit suggestion curated from a variety of fashion websites online.</p>
            <p>You can also provide a video link as a style reference.</p>
        </h2>
        </div>
        <form>
          <input
            type="text"
            value={query}
            onChange={handleQueryUpdate}
          >
          </input>
          {/* <div className="App">
            <h2>Upload photos from your wardrobe:</h2>
            <input type="file" onChange={handleChange} multiple="multiple"/>
            <img src={file}  width="200" alt=""/>
          </div> */}
        </form>
        <div>
          <Button variant="contained" color="primary" onClick={toggleText}>
            <h3>In Normal Mode</h3>
          </Button>
        </div>
      </div>
      </body>
    </div>
  );
}

export default GoShopping;