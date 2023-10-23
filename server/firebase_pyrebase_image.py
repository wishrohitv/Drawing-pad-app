import json

import pyrebase

with open('serviceAccount.json', 'r') as file_obj:
    f = json.load(file_obj)
config = {
    "apiKey": "AIzaSyAxiO8FrPTUF4I7PSR6i8ZlqXWJMeVyYxQ",
    "authDomain": "classmate-classes-f9057.firebaseapp.com",
    "databaseURL": "https://classmate-classes-f9057-default-rtdb.firebaseio.com",
    "projectId": "classmate-classes-f9057",
    "storageBucket": "classmate-classes-f9057.appspot.com",
    "messagingSenderId": "286165438643",
    "appId": "1:286165438643:web:658c70f981cf5b8cabe0c6",
    "measurementId": "G-18KW9VP3P6",
    "serviceAccount": f,
    "databaseUrl": "https://classmate-classes-f9057-default-rtdb.firebaseio.com/"
}
firebase_ = pyrebase.initialize_app(config)


# from plyer import filechooser
#
#
# def file():
#     filechooser.open_file(on_selection=selected)
#
#
# def selected(selection):
#     print(selection[0])
#     storage = firebase.storage()
#     storage.child('hello').put(selection[0])
#
#
# file()

# from firebase import firebase
#
# data = firebase.FirebaseApplication("https://classmate-classes-f9057-default-rtdb.firebaseio.com/", None)
#
# d = data.get("Physics", "")
# f = []
# for x in d.keys():
#     s = (d[x]["data_link"])
#     f.append(s)
# print(f)

# download
storage = firebase_.storage()
# storage.child('hello').put(selected)

storage.download(f"{f[0]}/11th", "pda.jpg.pdf.jpg")
#
# def image_load(lind_id, class_):
#     storage = firebase_.storage()
#     storage.download(f"{lind_id}/{class_}", f"chapter_visual_data/{lind_id}.jpg")
