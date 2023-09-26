import json

a = ["rohit"]
for i in a:
    print(i)
print([i for i in a])

with open('o.json') as f:
    data = json.load(f)
    print([{'text': x, 'name': data[x]['name']} for x in data])
