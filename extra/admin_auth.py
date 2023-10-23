import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)


email = input("enter email: ")
password = input("enter pass: ")
name = input("enter name: ")

try:
    user = auth.create_user(email=email, email_verified=True, password=password, display_name=name)
    print('{0} created successfully'.format(user.uid))
except Exception as f:
    print(f)



