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
                        year: seasonYear
                    }
                }
            }
        """

        variables = {
            "search": anime         
        }

        url = "https://graphql.anilist.co"

        response = requests.post(url, json={'query': query, 'variables': variables})
    except requests.RequestException:
        return None

    response = response.json()
    response = response["data"]["Page"]["media"]

    for r in response:
        if None in r.values():
            response.remove(r)

        # Shorten description
        else:
            r["desc"] = r["desc"].replace("<br>", "\n")
            r["desc"] = r["desc"].replace("\n\n", "\n")
            if len(r["desc"]) > 250:
                r["desc"] = r["desc"][:250] + "..."

    return response
