import smtplib
import random
import datetime as dt
my_email = "harbiodoon.ay@gmail.com"
password = "mjyjzpctdqphzups"

with open("quotes.txt") as file:
    quote_list = file.readlines()
    random_quote = random.choice(quote_list)

    today = dt.datetime.now()
    day = today.weekday()
    if day == 0:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="harbiodoon.ay@gmail.com",
                                msg=f"Subject:Motivational Quote\n\n {random_quote}"
                                )




