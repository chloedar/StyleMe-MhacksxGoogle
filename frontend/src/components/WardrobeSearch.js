import React from 'react';
import { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
// import "bootstrap/dist/css/bootstrap.min.css";
// import { FileUpload } from 'primereact/fileupload';   
// import "./App.css";     

const WardrobeSearch = () => {
//   const backgroundColor = "#f1d4ed";
//   const otherBackgroundColor = "#daf1d4";
  const [query, setQuery] = useState("");
  const [files, setFiles] = useState([]);
  const [sustainableBool, setSustainableBool] = useState(true);
  const [outputAvailable, setOutputAvailable] = useState(false);
  const [mode, setMode] = useState("wardrobe")

  const toggleText = () => {
    setSustainableBool(!sustainableBool);
  };

  function handleChange(e) {
    console.log(e.target.files);
    const updatedFiles = [...files]
    updatedFiles.push(URL.createObjectURL(e.target.files[0]));
    setFiles(updatedFiles);
    
    const formData = new FormData()
    formData.append('image', e.target.files[0]);

    const url = 'http://127.0.0.1:8000/upload/';
    fetch(url, {
      mode: 'cors',
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "http://localhost:3001",
      },
      body: formData,
    })
  };

  function handleQueryUpdate(e) {
    setQuery(e.target.value);
  };

  // function handleSubmit(e) {
  //   e.preventDefault();
    
  // };

  useEffect(() => {
    document.title = "StyleMe";
  }, []);

  function handleSubmit(e) {
    e.preventDefault();

    // var wardrobe = "wardrobe";
    
    const url = 'http://127.0.0.1:8000/outfit/';
    fetch(url, {
      mode: 'cors',
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "http://localhost:3001",
      },
      body: JSON.stringify({ query, mode })
    })
    .then((response) => {
      if (!response.ok) throw Error(response.statusText);
      return response.json();
    })
    .then((data) => {
      setOutputAvailable(true);
      // suggestedItems, links (list), and output parameters which is a string
    }   
    )
    setQuery("");
  }

  return (
    <>
      <title>
            StyleMe
      </title>
      <div>
        <h2>
            Build an outfit from your wardrobe!
        </h2>
        <div>
            <p>Type in the style or theme you're looking for.</p>
                {/* <p>You can also provide a video link as a style reference.</p> */}
        </div>
        <div>
          <form onSubmit={handleSubmit}>
              <input 
                  type="text"
                  value={query}
                  onChange={handleQueryUpdate}
                  style={{ marginBottom: '20px' }}
              >
              </input>
              <div className="App" style={{ textAlign: 'center' }}>
                <h3 style={{ display: 'inline-block', marginRight: '10px' }}>Upload photos from your wardrobe:</h3>
                <input type="file" onChange={handleChange} multiple="multiple" style={{ display: 'inline-block' }} />
                {/* <img src={files}  width="200" alt=""/> */}
                {files.map((file) => (<img src={file} width="200" alt="" style={{ display: 'block' }} />))}
              </div>
            </form>
        </div>
        <div className="gray-box">
          {outputAvailable ? (
              <p> There is output available </p>
            ) : null}
        </div>
      </div>
    </>
  );
}

export default WardrobeSearch;