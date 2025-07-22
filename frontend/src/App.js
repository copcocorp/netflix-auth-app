/* // src/App.js
import React from 'react';
import './App.css';
import Login from './Login';

function App() {
  return (
    <div className="App">
      <Login />
    </div>
  );
}

export default App; */

import React, { useState } from 'react';
import Login from './Login';
import MovieGallery from './MovieGallery';
function App() {
  const [token, setToken] = useState(null);
  return (
    <div className="App">
      {!token ? (
        <Login setToken={setToken} />
      ) : (
        <MovieGallery token={token} />
      )}
    </div>
  );
}
export default App;