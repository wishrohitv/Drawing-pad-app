from firebase import firebase
# classmate-classes
firebase = firebase.FirebaseApplication('https://classmate-classes-f9057-default-rtdb.firebaseio.com/', None)
data = {
    'chapter_index': 'english',
    'class': '12'
}

# post data
firebase.post('Subjects', data)
# get data
#result = firebase.get('classmate-classes-f9057-default-rtdb/subjects', '')
# for i in result.keys():
#     print(result[i]['class'])

#for i in result:
    #print(result[i]['chapter_index'])

