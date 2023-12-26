import requests
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
from io import BytesIO

class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather App")
        self.root.config(bg="light blue")
        self.root.minsize(width=800, height=350)

        city_query = simpledialog.askstring("Weather App", "Enter a city name:")

        params = {
            'access_key': 'af62b4d5875e47c3487c56d45aefe2d1',
            'query': city_query
        }

        api_result = requests.get('http://api.weatherstack.com/current', params)
        data = api_result.json()

        FONT = ("System", 23)

        # Temperature
        temperature = "Temperature:     " + str(data['current']['temperature']) + "°C"
        temperature_label = tk.Label(self.root, text=temperature, bg="light blue", fg="red", font=FONT)
        temperature_label.place(x=20, y=20, anchor="nw")

        # Feels Like
        feels_like = "Feels Like:     " + str(data['current']['feelslike']) + "°C"
        fl_label = tk.Label(self.root, text=feels_like, bg="light blue", fg="red", font=FONT)
        fl_label.place(x=20, y=60, anchor="nw")

        # Humidity
        humidity = "Humidity:      " + str(data['current']['humidity']) + "%"
        humidity_label = tk.Label(self.root, text=humidity, bg="light blue", fg="red", font=FONT)
        humidity_label.place(x=20, y=100, anchor="nw")

        # Wind Speed
        wind_speed = "Wind Speed:    " + str(data['current']['wind_speed']) + " km/h"
        wind_speed_label = tk.Label(self.root, text=wind_speed, bg="light blue", fg="red", font=FONT)
        wind_speed_label.place(x=20, y=140, anchor="nw")

        # Weather Description
        weather_desc = "Weather:       " + data['current']['weather_descriptions'][0]
        weather_desc_label = tk.Label(self.root, text=weather_desc, bg="light blue", fg="red", font=FONT)
        weather_desc_label.place(x=20, y=180, anchor="nw")

        # Wind Direction
        wind_direction = "Wind Direction: " + str(data['current']['wind_dir'])
        wind_direction_label = tk.Label(self.root, text=wind_direction, bg="light blue", fg="red", font=FONT)
        wind_direction_label.place(x=20, y=220, anchor="nw")

        # Pressure
        pressure = "Pressure:      " + str(data['current']['pressure']) + " hPa"
        pressure_label = tk.Label(self.root, text=pressure, bg="light blue", fg="red", font=FONT)
        pressure_label.place(x=20, y=260, anchor="nw")

        # Cloud Cover
        cloud_cover = "Cloud Cover:   " + str(data['current']['cloudcover']) + "%"
        cloud_cover_label = tk.Label(self.root, text=cloud_cover, bg="light blue", fg="red", font=FONT)
        cloud_cover_label.place(x=20, y=300, anchor="nw")

        # Weather Icon
        weather_icon_url = data['current']['weather_icons'][0]
        response = requests.get(weather_icon_url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((300, 300))
        photo = ImageTk.PhotoImage(img)

        icon_label = tk.Label(self.root, image=photo, bg="light blue")
        icon_label.image = photo
        icon_label.place(x=780, y=30, anchor="ne")

        self.root.mainloop()

if __name__ == "__main__":
    app = WeatherApp()
