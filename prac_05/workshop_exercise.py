from datetime import datetime
import random

# Universal Ride Ticketing System
MIN_AGE = 5
MAX_AGE = 50
WD_YOUNG = 30
WD_MID = 50
WD_OLD = 45
WK_YOUNG = 40
WK_MID = 60
WK_OLD = 55
WD_EXP = 20
WK_EXP = 30
GIFT_LIST = ["smartphone", "watch", "bicycle", "car", "movie ticket"]

print("*******************************\nUniversal Ride Ticketing System\n*******************************")
birthday = datetime.strptime(input("Enter birthday Eg: 1999/05/15 :"), "%Y/%m/%d")
today = datetime.today()
age = today.year - birthday.year

price = 0
standard = ""
signal_bool = True
while signal_bool:
    standard = input("Enter WD or WK: ").lower()
    if standard == "wd":
        signal_bool = False
        if age < MIN_AGE:
            price = WD_YOUNG
        elif age <= MAX_AGE:
            price = WD_MID
        else:
            price = WD_OLD
    elif standard == "wk":
        signal_bool = False
        if age < MIN_AGE:
            price = WK_YOUNG
        elif age <= MAX_AGE:
            price = WK_MID
        else:
            price = WK_OLD
    else:
        print("Invalid input!")

while not signal_bool:
    upgrade = input("Upgrade the ticket? YES/NO ").lower()
    if upgrade == "yes":
        signal_bool = True
        if standard == "wd":
            price += WD_EXP
        else:
            price += WK_EXP
    elif upgrade == "no":
        signal_bool = True
    else:
        print("Invalid input!")

if birthday.month == today.month:
    gift = random.choice(GIFT_LIST)
    print(f"Happy Birthday!! You won a {gift} as birthday present.")

print("Today is", today.strftime("%Y-%m-%d"))
print("The cost of your ticket is", price)
