import firebase_admin
from firebase_admin import credentials, storage, db

cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred, {"storageBucket": "classmate-classes.appspot.com",
                                     "databaseURL": "https://classmate-classes-default-rtdb.firebaseio.com/"})


def get_chapter_database(subject_name):
    ref = db.reference(f"/{subject_name}")
    return ref.get()


def upload_new_chapter_to_database(file, data_id, class_, subject, chapter_name, desc, date):
    bucket = storage.bucket()
    blob = bucket.blob(f"{str(data_id)}/{class_}")
    blob.upload_from_filename(file)
    print(f"File {file} uploaded to {data_id}/{class_}.")

    # datebase

    ref = db.reference(subject)
    ref.push({class_: {
        "class": class_,
        "chapter_name": chapter_name,
        "desc": desc,
        "upload_date": date,
        "data_link": str(data_id)
    }})
