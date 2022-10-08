import json
from functools import wraps

import requests
from flask import redirect, render_template, request, session


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def lookup(anime):

    # Contact API
    try:
        # Here we define our query as a multi-line string
        query = """
            query ($id: Int, $page: Int, $search: String) {
                Page (page: $page) {
                    media (id: $id, search: $search, type: ANIME) {
                        id
                        title {
                            english
                            romaji
                        }
                        desc: description
                        image: coverImage {
                            extraLarge
                        }
                        episodes
                        score: averageScore
                    }
                }
            }
        """

        # Define our query variables and values that will be used in the query request
        variables = {
            "search": anime         
        }

        url = "https://graphql.anilist.co"

        # Make the HTTP Api request
        response = requests.post(url, json={'query': query, 'variables': variables})
    except requests.RequestException:
        return None

    response = response.json()
    response = response["data"]["Page"]["media"]
    
    return response