import React, { FunctionComponent, useState } from 'react';
// import { theme } from '../../theme';
import './NLU.css';

export const NLU: FunctionComponent = () => {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [input, setInput] = useState<string>('');
  const [prediction, setPrediction] = useState<string>('');
  const placeholder = 'Is it sunny in Paris, France right now?';

  const handleChange = (event: any) => {
    setInput(event.target.value);
  };

  const handlePredict = () => {
    setIsLoading(true);
    fetch('http://127.0.0.1:5000/prediction/', {
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      method: 'POST',
      body: JSON.stringify({ sentence: input }),
    })
      .then((response) => response.json())
      .then((response) => {
        setPrediction(response.result);
        setIsLoading(false);
      })
      .catch((error) => console.error(error));
  };

  const _displayLoading = () => {
    if (isLoading) {
      return <p>Loading</p>;
    }
  };

  const show_input = (input: string) => {
    if (input.length > 0) {
      return input;
    }
  };

  return (
    <div className="NLU">
      <input className="input" onChange={handleChange} placeholder={placeholder} name="input" />
      <button className="button" onClick={handlePredict}>
        Analyze
      </button>
      <h1 className="field">Input</h1>
      {show_input(input)}
      <h1 className="field">Prediction</h1>
      {prediction}
    </div>
  );
};
