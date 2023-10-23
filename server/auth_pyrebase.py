import json

import pyrebase

config = {
    "apiKey": "AIzaSyAxiO8FrPTUF4I7PSR6i8ZlqXWJMeVyYxQ",
    "authDomain": "classmate-classes-f9057.firebaseapp.com",
    "databaseURL": "https://classmate-classes-f9057-default-rtdb.firebaseio.com",
    "projectId": "classmate-classes-f9057",
    "storageBucket": "classmate-classes-f9057.appspot.com",
    "messagingSenderId": "286165438643",
    "appId": "1:286165438643:web:658c70f981cf5b8cabe0c6",
    "measurementId": "G-18KW9VP3P6"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
try:
    user = auth.create_user_with_email_and_password('rohit@gmail.com', 'holaid')
    # user = auth.sign_in_with_email_and_password("rohit@gmail.com", "holaid")
    # print('successfully signed')
except Exception as e:
    print(e)
