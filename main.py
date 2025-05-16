import requests
from datetime import datetime, timezone
import smtplib
import time

MY_LAT = 35.831421
MY_LONG = 127.140388

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

hour_now = datetime.now(timezone.utc).hour

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])



while True:
    time.sleep(60)
    print(sunrise)
    print(sunset)
    print(hour_now)
    print(iss_latitude)
    print(iss_longitude)
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5 and sunset < hour_now < sunrise:

        MY_EMAIL = "testingmodule0@gmail.com"
        PASSWORD = "obte byhj ftar jodn"
        TO_EMAIL = "jaloliddinqulmatov12@gmail.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=TO_EMAIL,
                                msg="Subject:ISS Tracker\n\nLook up Bro!\nThe ISS is above your head.")
