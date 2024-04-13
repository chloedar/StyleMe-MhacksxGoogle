import React from 'react';
import { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
// import "bootstrap/dist/css/bootstrap.min.css";
// import { FileUpload } from 'primereact/fileupload';   
// import "./App.css";     

const WardrobeSearch = () => {
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
                Build an outfit from your wardrobe!
            </h1>
            <div>
                <h2>
                    <p>Upload images of your clothes and type in the style or theme you're looking for.</p>
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
            </div>
        </div>
        </body>
    </div>
  )
}

export default WardrobeSearch;