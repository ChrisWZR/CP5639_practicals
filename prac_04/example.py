"""
get birth_month
while birth_month < 1 or birth_month > 12
    display error message
    get birth_month

for count from 1 to birth_month
    display count
"""
MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12

# Using the format method:
month = int(input("Enter the month number ({}-{}): ".format(MINIMUM_MONTH, MAXIMUM_MONTH)))

# Using string concatenation and explicit type conversion
# month = int(input("Enter the month number (" + str(MINIMUM_MONTH) + "-" + str(MAXIMUM_MONTH) + "): "))

# Using f-strings
# month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
while month < MINIMUM_MONTH or month > MAXIMUM_MONTH:
    print("Invalid month")
    month = int(input("Enter your birth month: "))

for count in range(1, month + 1):
    print(count, end=" ")
print()
