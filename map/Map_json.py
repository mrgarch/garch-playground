import folium
import json

with open('json_sample.json') as f:
    data = dict(json.load(f))

print(data)

ids = [data[str(x)]['UID'] for x in range(10)]
print(ids)

lats = [data[str(x)]['latitude'] for x in range(10)]
print(lats)
longs = [data[str(x)]['longitude'] for x in range(10)]

my_map = folium.Map()

for i in range(len(data)):
    folium.Marker(location=[lats[i], longs[i]],
                  popup=ids[i],

                  ).add_to(my_map)

"""
for i in range(len(data)):
    folium.Marker(location=[lats[i], longs[i]],
                  popup=('<b>{}<b>'.format(names[i])),
                  icon=folium.Icon(color=colors[i], icon_color=icon_color[i], icon='train', prefix='fa')
                  ).add_to(cta_map)
"""
my_map.save('my_map2.html')


