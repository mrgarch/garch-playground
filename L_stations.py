# Folium train map


# 15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level.
# 5pts - Add the name to each stop as a popup. Add a train icon to each marker.  Save as an html page in the same folder.
# 3pts  - Color code all of the lines (make the pink line marker pink etc.)
# 2pts - Brown is not a default color name.  See if you can use the documentation for Folium to set a marker color through other means.

# Data set is in this folder, but can be found at: https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD

# Tricky parts of this one
## The location is in tuple format.  If you have trouble converting it, try this:
my_string = '(41.2, -87.9)'
my_tuple = eval(my_string)
print(my_tuple)
print(type(my_tuple))


# If you have extra time, try to put some html into the popup.

import folium
import csv
import html

with open('CTA_-_System_Information_-_List_of__L__Stops (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)

cta_map = folium.Map(location=[41.8781, -87.6298])

print(data.pop(0))

names = [x[2] for x in data]
lats = [float(eval(x[-1])[0]) for x in data]
longs = [float(eval(x[-1])[1]) for x in data]
colors = []
icon_color = []

for i in range(len(names)):
    if data[i][7] == "true":
        colors.append('red')
        icon_color.append('white')
    elif data[i][8] == "true":
        colors.append('blue')
        icon_color.append('white')
    elif data[i][9] == "true":
        colors.append('green')
        icon_color.append('white')
    elif data[i][10] == "true":
        colors.append('white')  # brown
        icon_color.append('saddlebrown')
    elif data[i][11] == "true":
        colors.append('purple')
        icon_color.append('white')
    elif data[i][12] == "true":
        colors.append('purple')
        icon_color.append('white')
    elif data[i][13] == "true":
        colors.append('white')  # yellow
        icon_color.append('yellow')
    elif data[i][14] == "true":
        colors.append('pink')
        icon_color.append('white')
    elif data[i][15] == "true":
        colors.append('orange')
        icon_color.append('white')
    else:
        colors.append('white')
        icon_color.append('white')

print(colors)
print(len(colors))
print(len(names))


for i in range(len(data)):
    folium.Marker(location=[lats[i], longs[i]],
                  popup="""<a href="https://google.com/maps/@{},{},18z"target="_blank",><b>{}<b></a>""".format(lats[i], longs[i], names[i]),
                  icon=folium.Icon(color=colors[i], icon_color=icon_color[i], icon='train', prefix='fa')
                  ).add_to(cta_map)

"""
for i in range(len(data)):
    folium.Marker(location=[lats[i], longs[i]],
                  popup=('<b>{}<b>'.format(names[i])),
                  icon=folium.Icon(color=colors[i], icon_color=icon_color[i], icon='train', prefix='fa')
                  ).add_to(cta_map)
"""
cta_map.save('my_cta_map.html')


