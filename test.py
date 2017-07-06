import json
f = open('result_landofnod_0629.json')
data = json.load(f)

for line in data:
    if 'width' in line:
        print line['width']