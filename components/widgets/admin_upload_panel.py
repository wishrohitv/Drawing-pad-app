import json
from kivy.uix.boxlayout import BoxLayout
from firebase import firebase
from plyer import filechooser
import pyrebase
import time
import uuid

date = time.asctime()
firebase = firebase.FirebaseApplication('https://classmate-classes-f9057-default-rtdb.firebaseio.com/', None)
data_id = uuid.uuid4()

# with open('serviceAccount.json', 'r') as f_obj:
#     serviceA = json.load(f_obj)
#     print(serviceA)
config = {
    "apiKey": "AIzaSyAxiO8FrPTUF4I7PSR6i8ZlqXWJMeVyYxQ",
    "authDomain": "classmate-classes-f9057.firebaseapp.com",
    "databaseURL": "https://classmate-classes-f9057-default-rtdb.firebaseio.com",
    "projectId": "classmate-classes-f9057",
    "storageBucket": "classmate-classes-f9057.appspot.com",
    "messagingSenderId": "286165438643",
    "appId": "1:286165438643:web:658c70f981cf5b8cabe0c6",
    "measurementId": "G-18KW9VP3P6",
    "serviceAccount": {
                          "type": "service_account",
                          "project_id": "classmate-classes-f9057",
                          "private_key_id": "c969e9daf02e22d90d8bb80552181a6819fcafbe",
                          "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCatW0Og/+x+G2l\nunNNT0AJ81PF99zHW/B5jwaWwRONfe8n8DSM9zddYwC4YRf30HGCufD9HFoknidm\nqTvr5PcsyCsDoZmgxsaVaYgSm+rcJcoea7qei4qluxO2zLBspj1HMcBg56J6Uvog\nC0zdzsIUgAhXUPwtTbTqTrOn2xTyepbRPZcYiHU66KmVi7t8ewZLpbFBnBtL4dX4\nBSF18IP/VPN3qU8GP1JKgElgod/btTm54C0cvpappGxuJffjduEEn0nNJanNkb9P\n461qI0W6GOfduCGuq1HVzdyqbxCJl0pq4nhy8gvpU2L1VNbLqa+wpgEYxzImas1d\nEgUKXwZbAgMBAAECggEAAX0GWBHoB1fLAkGpc1B0XsQjBbANRTO6vAimuRORcxaH\nkvxKHSMRusnFi4CPoPg151qPmXfI3DpTSbcOFwZkZF9mnonS9wuChJR31Sn/1+9b\nIvDJYlYYVuDWXzdX6SuuQj2VyrjfxMqAkodZTXb8QgM7UU+7pVnuiCSKsO44JN8K\nN5FowpMe1YypfbrJQpx2zhF7VN2p0dM91LBFoMGbf2pjjm+1RNHWcHSmbhBageYH\nHMGJQI0fBQ7OChs9mtsn9QSzevq8uCHSh8VYlPyfxX0+9Cj8eDj7RtRdtZix+mOO\nQLpFBHauKtqyjDgPLQfVhqHMGgYdpdRDergxNnkfmQKBgQDSiOdnmaKX6eA2TQF7\niNWk/PcxwrU221DhJnLn7Y1RTHXIGn7V5SSM7qMHT7hNh4MJZhfqYjqmpfv8niUC\nmzd97GMNekDhHn5Cjt1hIWm6zkLk7lG9Nb0D5b20ft5FvLWRDXb4/TK0SILqj1ro\nBkU7Y4hTg2ZjnOgVVUIlpm00swKBgQC8HkL4FF1GAKQlKsmYGeysAM+hQf/9njgt\nFO4Ps1SuUxhuOe/sBg+AAxxxFAumHzH7Obx7iXADbk+uLHbSuwwZvGiyM4qQtIpj\nIu1jFucdp2nUE8OF4oSI42sXVdTFfOF2qVZ87dniRbdWH3y3T9fyLvBPqS9nobSI\n8DFYua7LuQKBgQC02to+SuI7sbLjsp71agRtaMlIu8RDzX7bCtZmmdBt6Eq9jNUs\nFV2im1T88OSX5TMRndwpghx0D945kfilFoVC7Q/iAgU93Z4Euwk9aSCUUp9wXbFl\n4oXulSqzpNB4A7XNV02+cnNeH3Qm3uLusoRCkiwH4bbRF3be7JCYGzFwtQKBgG7r\nIO2JhF2sLxzDF86ZKpVYfRRGCByQV+ss9hlH0dxfnn4Pp0lxYV5Hd1OtUBkJN707\nk8j7hpJfTpgSG5WxODdMgibggQlFintdsr7EWE2B0sJ7TMP6hc742MIPl79CHOaM\nfjR3QgtKtAkR08V6TIe96W/u/8aI8Bv2FAKOqWPxAoGAZbUyZSbnwQ00L6IiLg+b\n56SOv+4K6le7vNfYj6CuQNtEMpKFVkmLNq8hLyBEY+xHP717ogFvZA1uWoLcRSZW\nnjelaPgQHV+KflJdF2ZujdTMMmdkGrcHiH4XJhaXYi4RuhPK7O97pxN5bVzeZMrh\n5dgxWsi6AhZOz2ZWoJAA8RE=\n-----END PRIVATE KEY-----\n",
                          "client_email": "firebase-adminsdk-252p1@classmate-classes-f9057.iam.gserviceaccount.com",
                          "client_id": "104493652156204028004",
                          "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                          "token_uri": "https://oauth2.googleapis.com/token",
                          "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                          "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-252p1%40classmate-classes-f9057.iam.gserviceaccount.com",
                          "universe_domain": "googleapis.com"},
    "databaseUrl": "https://classmate-classes-f9057-default-rtdb.firebaseio.com/"
}

file_local_dir = []


class UploadTabs(BoxLayout):
    def select_file(self):
        self.ids.upload_date.text = str(date)
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        self.ids.file_dir.text = selection[0]
        global file_local_dir
        file_local_dir.append(selection[0])

    def pushToDb(self, subject, class_, chapter_name, desc):
        data = {
            "class": class_,
            "chapter_name": chapter_name,
            "desc": desc,
            "upload_date": date,
            "data_link": str(data_id)
        }

        pyre = pyrebase.initialize_app(config)

        global file_local_dir
        # file = file_local_dir[-1]

        if subject == "select":
            self.ids.notice.text = "choose subject first!"
        elif class_ == "select":
            self.ids.notice.text = "choose class first!"
        elif chapter_name == "":
            self.ids.notice.text = "Write chapter name!"
        elif desc == "":
            self.ids.notice.text = "Write about Chapter!"
        elif self.ids.file_dir.text == "":
            self.ids.notice.text = "Please File first!"
        else:
            pass
            # media database
            # storage = pyre.storage()
            # storage.child(f"{str(data_id)}/{class_}").put(file)
            #
            # # database
            # firebase.post(subject, data)
