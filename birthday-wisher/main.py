import smtplib
import random
from time import sleep
import pandas as pd
import datetime as dt


today = dt.datetime.today()
month = today.month
day = today.day


my_email = "<EMAIL>"
my_password = "<PASSWORD>"

def send_email(to, body):
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(my_email, my_password)
    smtp_server.sendmail(my_email, to, body)
    smtp_server.quit()
    print("Email sent!")
    sleep(10)


df = pd.read_csv('birthdays.csv')
all_names = df.to_dict('records')


letters = []
for number in range(1, 4):
    with open(f"letter_templates/letter_{number}.txt", "r") as f:
        f = f.read()
        letters.append(f)



for person in all_names:
    if person["month"] == month and person["day"] == day:
        name = person["name"]
        text = random.choice(letters)
        text = text.replace("[NAME]", name)
        email = person["email"]
        send_email(to=email, body=text)
        print(text)
