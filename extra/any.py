from firebase import firebase

firebaseConfig = {
  "apiKey": "AIzaSyAHW4nxq2EwXzgDxMbzC8GMDIPTGkydQgI",
  "authDomain": "classmate-classes.firebaseapp.com",
  "databaseURL": "https://classmate-classes-default-rtdb.firebaseio.com",
  "projectId": "classmate-classes",
  "storageBucket": "classmate-classes.appspot.com",
  "messagingSenderId": "1097781563990",
  "appId": "1:1097781563990:web:e49ec95b23de1a5b8521f7",
  "measurementId": "G-8GY4M52Z3G"
}

firebase = firebase.FirebaseApplication('https://classmate-classes-default-rtdb.firebaseio.com/', authentication=None)
# result = firebase.get('/users', None, {'print': 'pretty'})

# print(result)

# >> {'error': 'Permission denied.'}

authentication = firebase.FirebaseAuthentication('AIzaSyAHW4nxq2EwXzgDxMbzC8GMDIPTGkydQgI', 'Joe@Tilsed.com', extra={'id': 123})
firebase.authentication = authentication
print(authentication.extra)
#
# # >> {'admin': False, 'debug': False, 'email': 'Joe@Tilsed.com', 'id': 123, 'provider': 'password'}
#
# user = authentication.get_user()
# print(user.firebase_auth_token)