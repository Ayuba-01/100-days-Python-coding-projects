import requests
from datetime import datetime
import smtplib

MY_LAT = 32.844017  # Your latitude
MY_LONG = -97.143066  # Your longitude


# Your position is within +5 or -5 degrees of the ISS position.
def iss_close_to_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude in range(round(MY_LAT), round(MY_LAT - 5)) and
            iss_longitude in range(round(MY_LONG), round(MY_LONG - 5))):
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


def send_email():
    with open("details.txt") as d:
        details = d.readlines()
        my_email = details[0].strip()
        my_password = details[1].strip()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:ISS Passing\n\n Look Up the ISS is passing above you !"
                            )


if is_dark() and iss_close_to_me():
    send_email()
