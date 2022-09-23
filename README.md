# animeee

### Description:
animeee is a personal online anime journal for anime enthusiasts to help keep track of their anime watchlists (watched, watching, favourites). It is built solely on Flask and works with the Jikan API on the backend. I built this project because I love anime and everything about it. I've always used MyAnimeList to discover anime and making this project with Jikan, which is an unofficial MyAnimeList API was really exciting.

### How it Works
To add anime to any of the watchlists, the user has to query the API in the `Search`. A request is made to Jikan with the search query and it returns about 50 results with titles that contain the exact or a related query. On adding to a watchlist, the title of the anime and the ID of the current logged in user is stored in the database.

### How to Run
To run this application, install the necessary packages with 
```
pip install -r requirements.txt
```
and you should be able to run the application with
```
flask run
```

### Contribution

I've curated a list of issues in the Issues tab for contribution. Clone the repository and open a pull request.
