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
        url = "https://jikan1.p.rapidapi.com/search/anime"

        querystring = {"q": anime}
        headers = {
            "X-RapidAPI-Key": "35ed5fd643msh2f7a35cb1726a4ep17f19djsn4d0c6f6291bb",
            "X-RapidAPI-Host": "jikan1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
    except requests.RequestException:
        return None

    # Parse response
    try:
        response = response.json()
        response = response["results"]
        responseList = []
        for result in response:
            responseList.append(result)
        return responseList
    except (TypeError, ValueError):
        return None



