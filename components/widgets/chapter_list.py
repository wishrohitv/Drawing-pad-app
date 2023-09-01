import json
from kivy.uix.recycleview import RecycleView


class ChapterList(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with open('demo/demo.json') as f:
            data = json.load(f)
            self.subject_details = [{'text': str(x), 'chapter_name': data[x]['name'], 'chapter_upload_date': data[x]["upload_date"], 'link': data[x]['link']} for x in data]


