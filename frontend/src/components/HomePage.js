import React from 'react';
import { useEffect, useState } from 'react';

const HomePage = () => {

  const [query, setQuery] = useState("");

  function handleQueryUpdate(e) {
    setQuery(e.target.value);
  }

  useEffect(() => {
    document.title = "StyleMe";
  }, []);

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
        <form>
          <input
            type="text"
            value={query}
            onChange={handleQueryUpdate}
          >
          </input>
        </form>
      </div>
      </body>
    </div>
  );
}

export default HomePage;