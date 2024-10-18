import pandas as pd
import datetime as dt
import random
import smtplib

with open("details.txt") as d:
    details = d.readlines()
    MY_EMAIL = details[0].strip()
    MY_PASSWORD = details[1].strip()

with open("birthdays.csv") as file:
    f = pd.read_csv(file)
    df = pd.DataFrame(f)

birthday_dict = {}

# For people with the same date
for index, row in df.iterrows():
    key = (row.month, row.day)
    if key not in birthday_dict:
        # Create a new list for this key if it doesn't exist
        birthday_dict[key] = [[row.person_name, row.email]]
    else:
        # Append the row to the existing list for this key
        birthday_dict[key].append([row.person_name, row.email])

today = dt.datetime.now()
today_month = today.month
today_day = today.day

if (today_month, today_day) in birthday_dict:
    people_details_list = birthday_dict[(today_month, today_day)]
    for detail_index in range(len(people_details_list)):
        random_number = random.randint(1, 3)
        with open(f"./letter_templates/letter_{random_number}.txt", "r") as letter:
            random_letter = letter.read()
            formatted_letter = random_letter.replace("[NAME]", f"{people_details_list[detail_index][0]}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=f"{people_details_list[detail_index][1]}",
                                msg=f"Subject:Happy Birthday\n\n {formatted_letter}"
                                )
