import React, { FunctionComponent } from 'react';
import './App.css';
import { NLU } from './components';

const App: FunctionComponent = () => {
  return (
    <div className="App">
      <header className="App-header">
        <p className="App-title">Natural Language Understanding</p>
        Web application in React, Typescript
      </header>
      <NLU />
    </div>
  );
};

export default App;
