"""
CP1401 2023 TR1 Assignment 1
Program 1 – Pizza Pay Calculator
Name: Zhirong Wang
Date started: 2023/04/23

Pseudocode:
display program title
get num_trip, num_min
money_trips = num_trip * $1.45
money_mins = num_min * $0.95
display num_trip, money_trips
display num_min, money_mins
total_money = money_trips + money_mins
display total_money
"""

MONEY_PER_TRIP = 1.45
MONEY_PER_MIN = 0.95

print("Warm Pizza Pay Calculator")
num_trip = int(input("Number of trips: "))
num_min = int(input("Number of minutes: "))
money_trips = round((num_trip * MONEY_PER_TRIP), 2)
money_mins = round((num_min * MONEY_PER_MIN), 2)
print(f"For {num_trip} trips, your pay is: $%.2f" % money_trips)
print(f"For {num_min} minutes, your pay is: $%.2f" % money_mins)
total_money = money_trips + money_mins
print("Your total pay is $%.2f" % total_money)
