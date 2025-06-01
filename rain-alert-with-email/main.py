import requests
from datetime import datetime
import smtplib

api_key = "<API-KEY>"
MY_EMAIL = "<SENDER-EMAIL>"
MY_PASSWORD = "<PASSWORD>"

parameters = {
    "lat" : "<LATITUDE>",
    "lon" : "<LONGITUDE>",
    "appid" : api_key,
    "units" : "metric",
    "exclude" : "current,minutely,daily"
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather = weather_data["list"]
print(hourly_weather)

def send_email(message):
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(MY_EMAIL, MY_PASSWORD)
    smtp_server.sendmail(from_addr=MY_EMAIL, to_addrs="<RECEIVER-MAIL>", msg=message)
    smtp_server.quit()
    print("Email sent!")

for hour in range(0, len(hourly_weather)):
    if hourly_weather[hour]["weather"][0]["id"] < 623:
        time = datetime.fromtimestamp(hourly_weather[hour]["dt"]).strftime('%H')
        weather_condition = hourly_weather[hour]["weather"][0]["description"]
        text = f"At {time} o'clock, it seems to be going to {weather_condition}. Bring an umbrella!"
        send_email(text)

