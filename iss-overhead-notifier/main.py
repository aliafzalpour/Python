import requests
import datetime
import smtplib
import time

MY_LAT = 35.73188253559403
MY_LONG = 51.351279765267954
MY_EMAIL = "aliafzalpour.info@gmail.com"
MY_PASSWORD = "pzmenzyjdeoiewmm"


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Tehran"
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


def iss_is_close():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def send_email():
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(MY_EMAIL, MY_PASSWORD)
    smtp_server.sendmail(from_addr=MY_EMAIL, to_addrs="afzalpour.al@gmail.com", msg="LOOK UP IN THE SKY!!!!!!!!")
    smtp_server.quit()
    print("Email sent!")


email_is_sent = False
while not email_is_sent:
    if iss_is_close() and is_night():
        send_email()
        email_is_sent = True
    else:
        print(f"WHERE IS THAT THING???\n{MY_LAT, MY_LONG}\n")
    time.sleep(60)
