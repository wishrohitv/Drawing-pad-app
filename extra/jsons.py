import json
with open('o.json') as f:
    data = json.load(f)
    nama = 1
    for name in data:
        print(data[name]['name'])
        nama = nama + 1
        print(nama)
