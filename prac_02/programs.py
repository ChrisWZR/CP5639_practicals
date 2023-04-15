# 1. Discount Price
"""
get original_price
discount = original_price * 0.2
new_price = original_price – discount
print new_price
"""
original_price = float(input("Original price: $"))
DISCOUNT_RATE = 0.2
"""discount = original_price * 0.2"""
discount = original_price * DISCOUNT_RATE
new_price = original_price - discount
print("The discounted price is $", new_price, sep="")

# 2. Kilometres to Miles
"""
get distance in km
conversion rate of km to mile = 0.621371
distance in mile = distance in km * conversion rate of km to mile
print distance in mile
"""
distance_in_km = float(input("Please input the distance in kilometres: "))
CONVERSION_RATE_KM_TO_MILE = 0.621371
distance_in_mile = distance_in_km * CONVERSION_RATE_KM_TO_MILE
print("The distance in mile is: ", distance_in_mile)
CONVERSION_RATE_MILE_TO_KM = 1.60934
distance_in_mile = distance_in_km / CONVERSION_RATE_MILE_TO_KM
print("The distance in mile is: ", distance_in_mile)

# 3. Holiday Cost
"""
get daily food cost, daily activity cost, number of days
hotel cost = 75
cost in total = (daily food cost + daily activity cost + hotel cost) * number of days
print cost in total
"""
daily_food_cost = float(input("Daily food cost: $"))
daily_activity_cost = float(input("Daily activities cost: $"))
number_of_days = int(input("Number of days: "))
HOTEL_COST = 75
cost_in_total = (daily_food_cost + daily_activity_cost + HOTEL_COST) * number_of_days
print("")
print("The trip will cost $", cost_in_total, sep="")

# 4. Deep Sleep Calculation (Percentage)
"""
get total sleep in seconds, deep sleep in seconds
percentage of deep sleep = deep sleep in seconds / total sleep in seconds
seconds in per minute = 60
number of minutes = total sleep in seconds // seconds in per minute
number of seconds = total sleep in seconds % seconds in per minute
total sleep = number of minutes + m + number of seconds + s
number of minutes = deep sleep in seconds // seconds in per minute
number of seconds = deep sleep in seconds % seconds in per minute
deep sleep = number of minutes + m + number of seconds + s
print deep sleep, total sleep
print percentage of deep sleep
"""
total_sleep_in_seconds = int(input("Total sleep in seconds: "))
deep_sleep_in_seconds = int(input("Deep sleep in seconds : "))
percentage_of_deep_sleep = deep_sleep_in_seconds / total_sleep_in_seconds
SECONDS_PER_MIN = 60
"""get numbers of minutes & seconds for total sleep"""
num_minutes = total_sleep_in_seconds // SECONDS_PER_MIN
num_seconds = total_sleep_in_seconds % SECONDS_PER_MIN
total_sleep = str(num_minutes) + 'm ' + str(num_seconds) + 's'
"""get numbers of minutes & seconds for deep sleep"""
num_minutes = deep_sleep_in_seconds // SECONDS_PER_MIN
num_seconds = deep_sleep_in_seconds % SECONDS_PER_MIN
deep_sleep = str(num_minutes) + 'm ' + str(num_seconds) + 's'
print("")
print("Deep sleep :", deep_sleep)
print("Total sleep:", total_sleep)
print("Percentage : ", percentage_of_deep_sleep * 100, '%', sep="")
