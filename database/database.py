import json
import os
import firebase_admin
from firebase_admin import credentials, storage, db, auth

cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred, {"storageBucket": "classmate-classes.appspot.com",
                                     "databaseURL": "https://classmate-classes-default-rtdb.firebaseio.com/"})


def get_chapter_database(subject_name):
    ref = db.reference(f"/{subject_name}")
    return ref.get()


def upload_new_chapter_to_database(file, data_id, class_, subject, chapter_name, desc, date):
    # media database
    bucket = storage.bucket()
    blob = bucket.blob(f"{str(data_id)}/{class_}")
    blob.upload_from_filename(file)
    blob.make_public()
    url = blob.public_url
    # print(f"File {file} uploaded to {data_id}/{class_}.")

    # resource datebase

    ref = db.reference(subject)
    ref.push({
        "class": class_,
        "chapter_name": chapter_name,
        "desc": desc,
        "upload_date": date,
        "data_path_dir": str(data_id),
        "data_path_link": str(url)
    })


file = []


def download_pdf_file_to_local(pdf_file_id, class_):
    global file
    file.append(pdf_file_id)
    path = f"{pdf_file_id}.pdf"
    check_file_exist = os.path.isfile(f"chapter_visual_data/{path}")
    if not check_file_exist:
        bucket = storage.bucket()
        blob = bucket.blob(f"{pdf_file_id}/{class_}")
        blob.download_to_filename(f"chapter_visual_data/{pdf_file_id}.pdf")
        print(f"File {'image.jpg'} downloaded to {'path/adminimage.jpg'}.")
    else:
        print("file already exist")


def create_an_new_account(new_name, new_class, new_email, new_passw):
    new_user = auth.create_user(email=new_email, email_verified=True, password=new_passw, display_name=new_name,
                                phone_number=None)

    ref = db.reference("User_data")

    ref.push({new_user.uid: {
        'name': new_name,
        'class': new_class,
        'email': new_email,
        'phone_number': "null",
        'user_profile_image': "null",
        'user_profile_image_link': "null",
        'post_right_not_available': True
    }})


def get_user_data(uid):
    with open('user.json', 'r') as f:
        datas = json.load(f)

    ref = db.reference(f"/User_data")
    data = ref.order_by_key().get()
    for key, val in data.items():
        # print('{0} => {1}'.format(key, val))
        print(val.get(uid))
        user_progress = val.get(uid)
        if user_progress is not None:
            datas[uid] = user_progress
            with open('user.json', 'w') as b:
                json.dump(datas, b)
