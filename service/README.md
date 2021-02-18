# Natural Language Understanding service on the Snips Voice Platform dataset

## Intent classification with following intents

- SearchCreativeWork (e.g. _Find me the I, Robot television show_)
- GetWeather (e.g. _Is it windy in Boston, MA right now?_)
- BookRestaurant (e.g. _I want to book a highly rated restaurant for me and my boyfriend tomorrow night_)
- PlayMusic (e.g. _Play the last track from Beyoncé off Spotify_)
- AddToPlaylist (e.g. _Add Diamonds to my roadtrip playlist_)
- RateBook (e.g. _Give 6 stars to Of Mice and Men_)
- SearchScreeningEvent (e.g. _Check the showtimes for Wonder Woman in Paris_)

### Setup requirements

```:bash
cd service
conda create -n flask_nlu_service python=3.7
conda activate flask_nlu_service
python3.7 -m pip install -r requirements.txt
```

### Runing the service

```:bash
FLASK_APP=app.py flask run
```

### Removing env

```:bash
conda deactivate
conda remove -n flask_nlu_service --all
```
