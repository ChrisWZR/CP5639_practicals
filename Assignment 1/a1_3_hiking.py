"""
CP1401 2023 TR1 Assignment 1
Program 3 – Hiking Tracker
Name: Zhirong Wang
Date started: 2023/04/23

Pseudocode:
set total_distance, average_distance, final_distance, msg(above/below/equal)
display program title
get num_day

repeat until num_day >= 1
    display Invalid number of days
    get num_day

repeat num_day times
    get distance

    repeat until distance is correct
        display Invalid distance
        get distance

    if i == num_day(get final_distance)
        final_distance = distance

    total_distance += distance

display total_distance
display average
if final_distance < average_distance
    display below
else if final_distance = average_distance
    display equal
else
    display above
"""
MINIMUM_DAY = 1
MINIMUM_DISTANCE = 0
MAXIMUM_DISTANCE = 120
total_distance = 0
average_distance = 0.0
final_distance = 0.0
msg = ""

print("Hiking Tracker")
num_day = int(input("Number of days: "))
while num_day < MINIMUM_DAY:
    print("Invalid number of days")
    num_day = int(input("Number of days: "))

for i in range(1, num_day + 1):
    distance = float(input(f"Day {i} distance: "))
    while not (MINIMUM_DISTANCE <= distance <= MAXIMUM_DISTANCE):
        print("Invalid distance")
        distance = float(input(f"Day {i} distance: "))
    if i == num_day:
        final_distance = distance
    total_distance += distance

print(f"\nYour total distance was {total_distance}km")
average_distance = total_distance / num_day
print(f"Your average distance was {average_distance}km")
if final_distance < average_distance:
    msg = "below"
elif final_distance == average_distance:
    msg = "equal"
else:
    msg = "above"
print(f"On your final day, your distance was {msg} average.")
