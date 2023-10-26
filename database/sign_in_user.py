import json
import os
import requests

FIREBASE_WEB_API_KEY = os.environ.get("AIzaSyAHW4nxq2EwXzgDxMbzC8GMDIPTGkydQgI")
rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"


def sign_in_with_email_and_password(email, password, return_secure_token: bool = True):

    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token
    })

    r = requests.post(rest_api_url,
                      params={"key": "AIzaSyAHW4nxq2EwXzgDxMbzC8GMDIPTGkydQgI"},
                      data=payload)

    return r.json()