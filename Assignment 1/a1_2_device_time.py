"""
CP1401 2023 TR1 Assignment 1
Program 2 – Device Time Determinator
Name: Zhirong Wang
Date started: 2023/04/23

Pseudocode:
display program title
get num_prac, do_mow(yes/no)
if do_mow == yes
    device_time = num_prac * 15min
    display device_time
    if num_prac >= 7
        display cupcake
else
    display no device time
"""
MIN_PER_PRAC = 15

print("Device Time Determinator")
num_prac = int(input("Number of practices: "))
do_mow = input("Did you mow? ").lower()
if do_mow == "yes":
    device_time = num_prac * MIN_PER_PRAC
    print(f"You get {device_time} minutes of device time :)")
    if num_prac >= 7:
        print("And you get a cupcake!")
else:
    print("No device time :(")
