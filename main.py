from tkinter import *
import tkinter as tk
import requests

# import tinker as a whole and after import tkinter as tk
# adding functionality to our app

base = Tk()

# we configure our app title and dimensions and background colour
base.title("Weather App Group 6")
base.configure(bg="#9bd7e8")
base.geometry("580x480")
# configure our rows and columns
base.rowconfigure(0, minsize=50)
base.columnconfigure([0, 1, 2, 3, 4], minsize=4)


'''start our fields and labels which will be displaying
the data'''
# title labels
title_1 = Label(text="Weather App", width=20, font=("bold", 30), bg="#9bd7e8")

title_2 = Label(text="Search for Weather of any city of your choice", width=32, font=("italics", 15), bg="#9bd7e8")
# Search field and button in grid format
city_name = StringVar()
search_city = tk.Entry(textvariable=city_name, text="Search for city")


def search_weather():
    api_key = "14ed2a78adcbcbfe1ac9d1ffb8c5eea6"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_names = search_city.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_names

    # response

    response = requests.get(complete_url)
    x = response.json()

    if['cod'] != '400':
        y = x['main']
        temp_High = y['temp_max']
        temp_Low = y['temp_min']
        pressure_value = y['pressure']
        hum_value = y['humidity']

        z = x['weather']
        description_weather = z[0]['description']

        m = x['sys']
        country_detail = m['country']

        temp_high_rs.configure(text=temp_High)
        temp_low_rs.configure(text=temp_Low)
        pres_rs.configure(text=pressure_value)
        hum_rs.configure(text=hum_value)
        des_rs.configure(text=description_weather)
        coun_rs.configure(text=country_detail)

    else:   # if there errors this will be executed
        temp_high_rs.configure(text="Error")
        temp_low_rs.configure(text="Error")
        pres_rs.configure(text="Error")
        hum_rs.configure(text="Error")
        des_rs.configure(text="Error")
        coun_rs.configure(text="Error")


button_search = tk.Button(text="Search", bg="white", command=search_weather)

# temp output and label

temp_high = Label(text="Temp(high) :", width=20, font=("bold", 20), bg="#9bd7e8")
temp_high_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")

temp_low = Label(text="Temp(low) :", width=20, font=("bold", 20), bg="#9bd7e8")
temp_low_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")
# pressure label and fetched data
pres = Label(text="Pressure :", width=20, font=("bold", 20), bg="#9bd7e8")
pres_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")
# humidity label and data
hum = Label(text="Humidity :", width=20, font=("bold", 20), bg="#9bd7e8")
hum_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")

# description
desc = Label(text="Description :", width=20, font=("bold", 20), bg="#9bd7e8")
des_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")
# country

coun = Label(text="Country :", width=20, font=("bold", 20), bg="#9bd7e8")
coun_rs = Label(text="", width=20, font=("bold", 20), bg="#9bd7e8")

# the grid lay out
title_1.grid(row=0, column=2)
title_2.grid(row=1, column=2)
search_city.grid(row=2, column=2)
button_search.grid(row=2, column=3)
temp_high.grid(row=3, column=2)
temp_high_rs.grid(row=3, column=3)
temp_low.grid(row=4, column=2)
temp_low_rs.grid(row=4, column=3)
pres.grid(row=5, column=2)
pres_rs.grid(row=5, column=3)
hum.grid(row=6, column=2)
hum_rs.grid(row=6, column=3)
desc.grid(row=7, column=2)
des_rs.grid(row=7, column=3)
coun.grid(row=8, column=2)
coun_rs.grid(row=8, column=3)
# to make the app run until its closed
base.mainloop()
