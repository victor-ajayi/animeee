# animeee
#### Video Demo:  https://youtu.be/Yo_PbeHOVqg

### Description:
animeee is a personal online anime journal for anime enthusiasts to help keep track of their anime watchlists (watched, watching, favourites). It is built solely on Flask and works with the Jikan API on the backend. I built this project because I love anime and everything about it. I've always used MyAnimeList to discover anime and making this project with Jikan, which is an unofficial MyAnimeList API was really exciting.

#### How it works
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

#### Improvements

One bad thing that stands out to me about this project is that is has absolutely no JavaScript. I had to seperate every function into routes in the Flask app. So to improve the usability of the app, implementing some and/or more features with JavaScript to declutter `app.py` would be great. Also, design wise, there's a lot that could be done. It has a fairly simple minimalistic design, which I like, but it definitely could use some design improvements.

The search route also needs improvements, right now it redirects immediately after adding an anime to a list. A much better implementation would be having it remain on the route so that multiple anime can be added at once.

I also have an idea of adding a comment section to the watched anime. Since the user has finished watching the anime, having the option to comment on it and talk about the experience would be nice. Having a shared list with other users is also something that could be added. Anime brings people together and sharing a watchlist would be great.

### Contribution

If you would like to contribute, a good place to start would be ideas in the *Improvements* section above. Clone the repository and open a pull request.