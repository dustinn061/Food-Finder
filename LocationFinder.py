import urllib.request
import webbrowser
import math
import re
from tkinter import *
root = Tk() # blank window

global place

var1 = IntVar()
c1 = Checkbutton(root, text='Arbys', variable=var1)
c1.grid(row=0)

var2 = IntVar()
c2 = Checkbutton(root, text='Wendys', variable=var2)
c2.grid(row=1)

var3 = IntVar()
c3 = Checkbutton(root, text='FiveGuys', variable=var3)
c3.grid(row=2)

var4 = IntVar()
c4 = Checkbutton(root, text='Chick Fil A', variable=var4)
c4.grid(row=3)

result1 = Message(root,text='Weather: ')
result1.grid(row=2,column=4)

entry1 = Entry(root)
entry1.grid(row=1,column=2)
def weather(self):
    base_url = 'https://forecast.weather.gov/zipcity.php?inputstring='
    url = base_url + entry1.get()
    stream = urllib.request.urlopen(url)

    line_finder = re.compile(r'<div class="row row-odd row-forecast">')
    for line in stream:
        line = line.decode('utf-8')
        if line_finder.search(line) != None:
            line = line.replace("<div class=\"row row-odd row-forecast\"><div class=\"col-sm-2 forecast-label\"><b>", '')
            line = line.replace("</b></div><div class=\"col-sm-10 forecast-text\">", ': ')
            line = line.replace("</div></div><div class=\"row row-even row-forecast\"><div class=\"col-sm-2 forecast-label\"><b>",'')
            line = line.replace("</div></div>", '')
            line = line.replace("</div>", '')
            result1.config(text= 'Weather: ' + line )
'''--------------------------------------------------------------------------------'''
def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees
    return dist


def fastfood(self):
    base_url_2 = 'https://www.google.com/maps/place/'
    stream = urllib.request.urlopen(base_url_2 + entry1.get())
    print(entry1.get())
    line_finder2 = re.compile(r';window.APP_INITIALIZATION_STATE=')

    for line in stream:
        line = line.decode('utf-8')
        if line_finder2.search(line) != None:
            line = line.replace(';window.APP_INITIALIZATION_STATE=[[[','')
            line = line.replace(']','')
            line = line.split(',')
            user_lon = float(line[1])
            user_lat = float(line[2])

    smallest_dist = 1000000000000000000000000000000
    smallest_address = None

    fillerUVA = 'http://cs1110.cs.virginia.edu/files/'

    website = urllib.request.urlopen(fillerUVA + self)

    for line in website:
        line = line.decode('utf-8')
        cells = line.split(',')
        poi_lat = float(cells[0])
        poi_lon = float(cells[1])
        dist = distance_between(user_lat, user_lon, poi_lat, poi_lon)
        if dist < smallest_dist:
            smallest_dist = dist
            smallest_address = cells[4] + cells[5] + cells[6]

        if ' ' in smallest_address:
            smallest_address = smallest_address.replace(' ', '+')

    smallest_address = 'http://maps.google.com/maps?q=' + smallest_address

    webbrowser.open(smallest_address)

def doStuff(event):
    if var1.get() == 1:
        place = 'arbys.csv'
        fastfood(place)

    if var2.get() == 1:
        place = 'wendys.csv'
        fastfood(place)



    if var3.get() == 1:
        place = 'fiveguys.csv'
        fastfood(place)


    if var4.get() == 1:
        place = 'chickfila.csv'
        fastfood(place)



button1 = Button(root, text='Get weather')
button1.bind("<Button-1>", weather)
button1.grid(row=4, column=1)

button2 = Button(root, text='Get Food')
button2.bind("<Button-1>", doStuff)
button2.grid(row=5, column=1)

root.title('I\'m Hungry')
root.mainloop()