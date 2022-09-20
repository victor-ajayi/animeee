# animeee
#### Video Demo:  https://youtu.be/Yo_PbeHOVqg

### Description:
animeee is a personal online anime journal for anime enthusiasts to help keep track of their anime watchlists (watched, watching, favourites). It is built solely on Flask and works with the Jikan API on the backend. I built this project because I love anime and everything about it. I've always used MyAnimeList to discover anime and making this project with Jikan, which is an unofficial MyAnimeList API was really exciting.

### How it works
To add anime to any of the watchlists, the user has to query the API in the `Search`. A request is made to Jikan with the search query and it returns about 50 results with titles that contain the exact or a related query. On adding to a watchlist, the title of the anime and the ID of the current logged in user is stored in the `data.db` database.

The project contains the following main files and folders:

`app.py`
This is the main Python file. Containing all the routes for basic functionality of the Flask app.

`helpers.py`
This file contains helper functions such as the `lookup` function for querying the API and `login_required` for making sure only logged in users are able to access to app.

`templates/ folder`
This directory contains all the template HTML for creating pages dynamically.

`static/ folder`
This contains a single `styles.css` file which has all the CSS styling rules for all the HTML file and is linked in the `layout.html`

### How to Run
To run this application, make sure you have [Flask](https://pypi.org/project/Flask/) installed and use the simple command in the terminal and it should open an instance in your default browser
```
flask run
```

### Contribution

I've curated a list of issues in the Issues tab for contribution. Clone the repository and open a pull request.
