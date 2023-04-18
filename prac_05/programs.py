# Input, Processing, Output
# 1. Percentage change
"""
get original_num, change
result = original_num * (1 + change)
display original_num, change, result
"""
original_num = float(input("Original: "))
change = float(input("Change: "))
result = original_num * (1 + change)
print(f"Original: {original_num}, Change: {change}, Result: {result}")

# Decision Structures
# 2. Time of day
"""
get time_of_day, coming_or_going
if time_of_day < 12
    time_str = before noon
else
    time_str = after noon

if coming_or_going == "coming"
    coming_str = Hi
else
    coming_str = Bye
display f'It is {time_str} and you are {coming_or_going}. {coming_str}!'
"""
time_of_day = int(input("The time of day (0-23 hours): "))
coming_or_going = input("Coming or going: ").lower()
if time_of_day < 12:
    time_str = "before noon"
else:
    time_str = "after noon"

if coming_or_going == "coming":
    coming_str = "Hi"
else:
    coming_str = "Bye"

print(f"It is {time_str} and you are {coming_or_going}. {coming_str}!")

# 3. Coffee orders
"""
get coffee_type, coffee_size
lower_prices = {'small': 3, 'medium': 4, 'large': 5}

if coffee_type = black
    if coffee_size in lower_prices
        price = lower_prices.get(coffee_size)
    else
        price = maximum value of lower_prices
else
    if coffee_size in lower_prices
        price = lower_prices.get(coffee_size) + 1
    else
        price = maximum value of lower_prices + 1
    
display price
"""
lower_prices = {'small': 3, 'medium': 4, 'large': 5}
price = 0
price_difference = 1

coffee_type = input("The type of coffee (black/white): ").lower()
coffee_size = input("The size of coffee (small/medium/large): ").lower()

if coffee_type == "black":
    if coffee_size in lower_prices:
        price = lower_prices.get(coffee_size)
    else:
        price = max(lower_prices.values())
else:
    if coffee_size in lower_prices:
        price = lower_prices.get(coffee_size) + price_difference
    else:
        price = max(lower_prices.values()) + price_difference

print("The price of coffee is $", price, sep="")

# Repetition Structures
# 4. Coffee orders with error-checking

lower_prices = {'small': 3, 'medium': 4, 'large': 5}
types = ["black", "white"]
price = 0
price_difference = 1
coffee_type = ""
coffee_size = ""
type_error_msg = ""
size_error_msg = ""
error_msg = ""

while not (coffee_type in types):
    coffee_type = input(f"{type_error_msg}The type of coffee (black/white): ").lower()
    type_error_msg = "Invalid choice\n"

while not (coffee_size in lower_prices):
    coffee_size = input(f"{size_error_msg}\nThe size of coffee (small/medium/large): ").lower()
    size_error_msg = "Invalid choice\n"

if coffee_type == "black":
    price = lower_prices.get(coffee_size)
else:
    price = lower_prices.get(coffee_size) + price_difference

print("The price of coffee is $", price, sep="")

# 5. Accumulation
"""
get low, high
if high < low
    display error
else
    for i from low to high
        display i
        total += i
    display total
"""
low = int(input("Low value: "))
high = int(input("High value: "))

if high < low:
    print("Error number.")
else:
    total = 0
    for i in range(low, high + 1):
        print(i, end=' ')
        total += i

    print(f"\nTotal: {total}")
