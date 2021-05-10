import json
import random
import uuid

"""
data = [(random.uniform(-90, 90), random.uniform(-180, 180), str(uuid.uuid4()))for x in range(100)]
json_string = json.dumps(data)
print(json_string)

json_string.save('map_json.json')
"""

data = {}
for i in range(10):
    data[i] = {}
    data[i]['UID'] = str(uuid.uuid4())
    data[i]['latitude'] = random.uniform(-90, 90)
    data[i]['longitude'] = random.uniform(-180, 180)

print(data)

with open("json_sample.json", "w") as f:
    json.dump(data, f)
