import React from 'react';
import { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
// import "bootstrap/dist/css/bootstrap.min.css";
// import { FileUpload } from 'primereact/fileupload';   
// import "./App.css";     

const GoShopping = () => {
  // const backgroundColor = "#f1d4ed";
  // const otherBackgroundColor = "#daf1d4";
  const [query, setQuery] = useState("");
  const [sustainableBool, setSustainableBool] = useState(true);
  const [outputAvailable, setOutputAvailable] = useState(false);
  const [mode, setMode] = useState("sustain");

  const toggleText = () => {
    setSustainableBool(!sustainableBool);
    setMode(sustainableBool ? "sustain" : "search_web");
  };

  function handleQueryUpdate(e) {
    setQuery(e.target.value);
  }

  function handleSubmit(e) {
    e.preventDefault();

    // var mode_to_send = (sustainableBool ? "sustain" : "search_web");

    const url = 'http://127.0.0.1:5000/outfit/';
    // onsole.log(mode_to_send)
    console.log(query)
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
      console.log("inside handleSubmit");
      setOutputAvailable(true);
      // suggestedItems, links (list), and output parameters which is a string
    }   
    )
    setQuery("");
  }

  // search_web: {"shiny heels":"https://www.nordstrom.com/sr/glitter-high-heels%21","sparkly dress":"https://www.amazon.com/Sparkle-Dresses/s?k=Sparkle+Dresses","statement earrings":"https://www.kendrascott.com/jewelry/statement-earrings/"}
  // sustain: {"links":["https://www.thredup.com/featured/154093049?department_tags=juniors&referral_code=adwords_pla%2Cadwords_pla&iv_=__iv_p_1_a_19641507037_g__c__w__n_x_d_c_v__l__t__r__x_pla_y_8908102_f_online_o_151141830_z_US_i_en_j__s__e__h_9016852_ii__gg__vi__&gclsrc=aw.ds&gad_source=4&gclid=Cj0KCQjw2uiwBhCXARIsACMvIU2aroiu_fQVENG5mcdy0sYFzsOPsADd5OxF8RmH1HQZfbd-UEOSqeYaAppqEALw_wcB&featured_item=154093049","https://www.depop.com/products/aswithin-silver-chrome-color-shifting-rainbow/"],"outfitParameter":"For a dazzling prom look, go with the sequin dress and platform shoes. The sequins will catch the light beautifully, and the platforms will add height and drama.","suggestedItems":["sequin dress","platform shoes"]}
  // wardrobe: {"message": output, "0":img, "1":img}
  useEffect(() => {
    document.title = "StyleMe";
  }, []);

  if (sustainableBool) {
    return (
      <div>
        <title>
          StyleMe
        </title>
        <div>
          <h1>
            Build a brand new outfit!
          </h1>
          <div>
            <p>Type in the style you're looking for to receive an outfit suggestion curated from SUSTAINABLE fashion websites online.</p>
            {/* <p>You can also provide a video link as a style reference.</p> */}
          </div>
          <form onSubmit={handleSubmit}>
            <p> Type in a request! </p>
            <input
              type="text"
              value={query}
              onChange={handleQueryUpdate}
            >
            </input>
          </form>
          <div>
            <Button variant="contained" color="primary" onClick={toggleText}>
              <h3>In Sustainable Mode</h3>
            </Button>
          </div>
          {outputAvailable ? (
            <p> There is output available </p>
          ) : null}
        </div>
      </div>
    );
  }
  return (
    <div>
      <title>
        StyleMe
      </title>
      <div>
        <h1>
          Build a brand new outfit!
        </h1>
        <div>
            <p>Type in the style you're looking for to receive an outfit suggestion curated from a variety of fashion websites online.</p>
            {/* <p>You can also provide a video link as a style reference.</p> */}
        </div>
        <form onSubmit={handleSubmit}>
          <p> Type in a request! </p>
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
    </div>
  );
}

export default GoShopping;