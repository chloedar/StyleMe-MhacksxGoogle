import React from 'react';
import { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
// import "bootstrap/dist/css/bootstrap.min.css";
// import { FileUpload } from 'primereact/fileupload';   
// import "./App.css";     

const HomePage = () => {

  const [query, setQuery] = useState("");
  const [file, setFile] = useState();
  // const [sustainableState, setSustainableState] = useState("In Sustainable Mode");
  const [sustainableBool, setSustainableBool] = useState(true);

  // useEffect(() => {
  //     setSustainableBool(true)
  //   return () => {
  //     // This is a cleanup function
  //   };
  // }, []);

  const toggleText = () => {
    // setSustainableBool((state) => !state);
    setSustainableBool(!sustainableBool);
    // setSustainableState((state) => (sustainableBool ? "In Sustainable Mode" : "Normal Mode "));
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
      <div>
        <title>
          StyleMe
        </title>
        <body>
        <div>
          <header>
            <h1>Welcome to StyleMe</h1>
          </header>
          <h1>
            Build an outfit from your wardrobe
          </h1>
          <div>
          <h2>
            Use this search bar to build an outfit from the clothes already in your closet!
            Upload images of your clothes and type in the style you're looking for.
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
          {/* <div>
            <FileUpload name="demo[]" url={'/'} multiple accept="image/*" maxFileSize={1000000} emptyTemplate={<p className="m-0">Drag and drop files to here to upload.</p>} />
          </div> */}
          {/* <div className="container" style={{ width: "600px" }}>
            <div className="my-3">
              <h3>bezkoder.com</h3>
              <h4>React Hooks Drag & Drop File Upload</h4>
            </div>
            <FileUpload />
          </div> */}
          {/* <div> */}
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
    <div>
      <title>
        StyleMe
      </title>
      <body>
      <div>
        <header>
          <h1>Welcome to StyleMe</h1>
        </header>
        <h1>
          Build an outfit from your wardrobe
        </h1>
        <div>
        <h2> this is a trial </h2>
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
        {/* <div>
          <FileUpload name="demo[]" url={'/'} multiple accept="image/*" maxFileSize={1000000} emptyTemplate={<p className="m-0">Drag and drop files to here to upload.</p>} />
        </div> */}
        {/* <div className="container" style={{ width: "600px" }}>
          <div className="my-3">
            <h3>bezkoder.com</h3>
            <h4>React Hooks Drag & Drop File Upload</h4>
          </div>
          <FileUpload />
        </div> */}
        {/* <div> */}
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

export default HomePage;