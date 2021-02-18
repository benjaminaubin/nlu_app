export function getPredictionFromApiWithSearchedText(text) {
    return fetch('http://127.0.0.1:5000/prediction/', 
      {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({sentence: text})
      })
      .then(response => response.json())
    .catch((error) => console.error(error))
  }