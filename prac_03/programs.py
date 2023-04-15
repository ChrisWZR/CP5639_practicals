# 1. Tax
"""
get income
if income < 100
    pay no tax
else if 100 <= income < 1000
    total_tax = income * 5%
else
    total_tax = income * 10%
"""
TAX_RATE_MID = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000

TAX_RATE_LOW = 0.02  # 2%
TAX_THRESHOLD_MID = 500

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
# TODO: complete this part of the program here
if income < TAX_THRESHOLD_LOW:
    total_tax = 0
elif TAX_THRESHOLD_LOW <= income < TAX_THRESHOLD_MID:   # 100 <= income < 500
    total_tax = income * TAX_RATE_LOW
elif TAX_THRESHOLD_MID <= income < TAX_THRESHOLD_HIGH:  # 500 <= income < 1000
    total_tax = income * TAX_RATE_MID
else:                                                   # 1000 <= income
    total_tax = income * TAX_RATE_HIGH
take_home_pay = income - total_tax

print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")

# 2. Car Insurance
"""
get age
if age < 18
    display Hire refused
else if 18 <= age < 25  # age < 25
    display Insurance required
else
    display Insurance not required
"""
print("Car Insurance Program")
age = int(input("Age:"))
if age < 18:
    print("Hire refused")
elif age < 25:
    print("Insurance required")
else:
    print("Insurance not required")

# 3. Simple Password Checker
"""
set REAL_PASSWORD
get entered_password
if entered_password == REAL_PASSWORD
    display Access granted
else
    display Access denied
"""
REAL_PASSWORD = "admin"
print("Simple Password Checker Program")
entered_password = input("Password:")
if entered_password == REAL_PASSWORD:
    print("Access granted")
else:
    print("Access denied")

# 4. Dog Years
"""
set FIRST_TWO_YEAR = 2
set FIRST_TWO_RATE = 10.5
set AFTER_TWO_RATE = 4

get human_age
if human_age <= FIRST_TWO_YEAR
    dog_age = FIRST_TWO_RATE * human_age
else
    dog_age = FIRST_TWO_RATE * FIRST_TWO_YEAR + AFTER_TWO_RATE * (human_age - FIRST_TWO_YEAR)
display dog_age
"""
FIRST_TWO_YEAR = 2
FIRST_TWO_RATE = 10.5
AFTER_TWO_RATE = 4

print("Dog Years Program")
human_age = int(input("Age in human years:"))
if human_age <= FIRST_TWO_RATE:
    dog_age = FIRST_TWO_RATE * human_age
else:
    dog_age = FIRST_TWO_RATE * FIRST_TWO_YEAR + AFTER_TWO_RATE * (human_age - FIRST_TWO_YEAR)
print("Age in dog years is", dog_age)

# 5. Rock of Ages
"""
get age
if 0 <= age <= 120
    if 0 <= age < 13
        display Children
    elif 13 <= age < 18
        display Adolescents
    elif 18 <= age < 65
        display Adults
    else
        display Elderly person
else
    display Invalid age
"""
MIN_AGE = 0
MAX_AGE = 120
MIN_ADOLESCENT = 13
MIN_ADULT = 18
MIN_ELDERLY = 65

print("Rock of Ages Program")
age = float(input("Age:"))
if MIN_AGE <= age <= MAX_AGE:
    if MIN_AGE <= age < MIN_ADOLESCENT:
        print("Child")
    elif MIN_ADOLESCENT <= age < MIN_ADULT:
        print("Adolescent")
    elif MIN_ADULT <= age < MIN_ELDERLY:
        print("Adult")
    else:
        print("Elderly person")
else:
    print("Invalid age")

# 6. Speeding Fines
"""
get total_speed,speed_limit
over_speed = total_speed - speed_limit
if 0 < over_speed < 13
    fine = $177
elif 13 <= over_speed <= 20
    fine = $266
elif 20 < over_speed <= 30
    fine = $444
elif 30 < over_speed <= 40
    fine = $622
else:
    fine = $1,245
display fine
"""
print("Speeding Fines Program")
total_speed = float(input("Speed (km/h):"))
speed_limit = float(input("Speed limit (km/h):"))
over_speed = total_speed - speed_limit
if 0 < over_speed < 13:
    fine = 177
elif 13 <= over_speed <= 20:
    fine = 266
elif 20 < over_speed <= 30:
    fine = 444
elif 30 < over_speed <= 40:
    fine = 622
else:
    fine = 1245
print("The fine is $", fine, sep="")
