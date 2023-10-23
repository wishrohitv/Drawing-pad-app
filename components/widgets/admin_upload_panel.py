from kivy.uix.boxlayout import BoxLayout
from plyer import filechooser
import time
import firebase_admin
from firebase_admin import credentials, storage, db
from database.database import upload_new_chapter_to_database

date = time.asctime()

file_local_dir = []


class UploadTabs(BoxLayout):
    def select_file(self, filename):
        global file_local_dir
        self.ids.file_dir.text = filename[0]
        file_local_dir.append(filename[0])

    # def select_file(self):
    #     self.ids.upload_date.text = str(date)
    #     filechooser.open_file(on_selection=self.selected)
    #
    def selected(self, selection):
        self.ids.file_dir.text = selection[0]
        global file_local_dir
        file_local_dir.append(selection[0])

    def pushToDb(self, subject, class_, chapter_name, desc):
        import uuid
        data_id = uuid.uuid4()

        global file_local_dir

        if subject == "select":
            self.ids.notice.text = "choose subject first!"
        elif class_ == "select":
            self.ids.notice.text = "choose class first!"
        elif chapter_name == "":
            self.ids.notice.text = "Write chapter name!"
        elif desc == "":
            self.ids.notice.text = "Write about Chapter!"
        elif len(file_local_dir) == 0:
            self.ids.notice.text = "Please select file!"
        elif self.ids.file_dir.text == "":
            self.ids.notice.text = "Please select File!"
        else:
            try:
                file = file_local_dir[-1]
                # print(file)
                # media database
                upload_new_chapter_to_database(file, data_id, class_, subject, chapter_name, desc, date)
                # bucket = storage.bucket()
                # blob = bucket.blob(f"{str(data_id)}/{class_}")
                # blob.upload_from_filename(file)
                # print(f"File {file} uploaded to {data_id}/{class_}.")
                # blob.make_public()
                # print(blob.public_url)

                # realtime database
                # ref = db.reference(subject)
                # ref.push({class_: {
                #     "class": class_,
                #     "chapter_name": chapter_name,
                #     "desc": desc,
                #     "upload_date": date,
                #     "data_link": str(data_id)
                # }})

                self.ids.notice.text = "successfully uploaded!"
                self.ids.subject.text = "select"
                self.ids.class_.text = "select"
                self.ids.chapter_name.text = ""
                self.ids.desc.text = ""
                self.ids.file_dir.text = ""
                # notice_popup()
            except Exception as f:
                # self.ids.notice.text = f
                print(f)
