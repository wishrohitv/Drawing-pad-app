import json

from firebase import firebase

# classmate-classes
firebase = firebase.FirebaseApplication('https://classmate-classes-f9057-default-rtdb.firebaseio.com/', None)
data = {
    'chapter_index': 'english',
    'class': '12'
}

# post data
# firebase.post('Subjects', data)
# get data
# result = firebase.get('classmate-classes-f9057-default-rtdb/Chemistry', '')
# result = firebase.get("https://classmate-classes-f9057-default-rtdb.firebaseio.com/", "")
# print(result)
# for i in result.keys():
#     print(i)

# for i in result:
#   print(result[i]['chapter_index'])

# result = firebase.delete("/Physics", "NdLjKFXgj7juaH6gbg2")
# print(result == None)

# with open('data.json', 'w') as f:
#     json.dump(result, f)

# with open('data.json') as s:
#     s = json.load(s)
#     for x in s.keys():
#         print(s["Physics"])
# # print(s["Physics"])
