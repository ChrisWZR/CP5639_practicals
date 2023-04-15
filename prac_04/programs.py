# 1. Error Checking
"""
get worker_level
while worker_level < 1 or worker_level > 10
    display error message
    get worker_level

for count from 1 to worker_level
    display salary      # salary = count * 5000
"""
MINIMUM_LEVEL = 1
MAXIMUM_LEVEL = 10
BASIC_SALARY = 5000

level = int(input("Worker level: "))

while level < MINIMUM_LEVEL or level > MAXIMUM_LEVEL:
    print("Invalid worker level")
    level = int(input("Worker level: "))

print(f"With worker level {level}, your salary is ${level * BASIC_SALARY:,.2f}")

# 2. Number Sequences
# a.
for i in range(1, 101, 2):
    print(i)

# b.
for i in range(1896, 2023, 4):
    print(i, end=" ")

# c.
"""This is a loop that generates all the years with a 28-day February from 1990 to 2023"""
for year in range(1990, 2023 + 1):

    # the year is not a leap year
    if year % 4 != 0:
        print(year)

# 3. Menus
"""
is_finished = False

while not is_finished
   get user_input
   if user_input == 's'
        display Smiley
    else if user_input == 'f'
        display Frowny
    else if user_input == 'q'
        is_finished = True
        display Farewell
    else
        display Invalid choice
"""
is_finished = False

while not is_finished:
    user_input = input("(S)miley\n(F)rowny\n(Q)uit\n").lower()
    if user_input == 's':
        print(":)")
    elif user_input == 'f':
        print(":(")
    elif user_input == 'q':
        is_finished = True
        print("Farewell")
    else:
        print("Invalid choice")

# 4. Accumulation
# Average Age
"""
SENTINEL = -1
total = 0
number = 0

get age
while age != SENTINEL
    total = total + age
    number += 1
    get age
display average     # average = total / number
"""
SENTINEL = -1
total = 0
number = 0

age = int(input("Enter age: "))
while age != SENTINEL:
    total = total + age
    number += 1
    age = int(input("Enter age: "))

average_age = total / number
print("The average age is:", average_age)

# Smileys Count

is_finished = False
number_smiley = 0
number_frowny = 0

while not is_finished:
    user_input = input("(S)miley\n(F)rowny\n(Q)uit\n").lower()
    if user_input == 's':
        number_smiley += 1
        print(":)")
    elif user_input == 'f':
        number_frowny += 1
        print(":(")
    elif user_input == 'q':
        is_finished = True
        print("Farewell")
    else:
        print("Invalid choice")
print(f"{number_smiley} smileys, {number_frowny} frownies.")

# Total Numbers
"""
total_number = 0
get count
repeat count times
    get number
    total_number = total_number + number
display total_number
"""
total_number = 0

count = int(input("How many numbers do you want to add up? "))
for i in range(1, count + 1):
    number = int(input(f"Enter number {i}: "))
    total_number += number
print(f"The total of those {count} numbers is {total_number}")

# 5. Guessing Game
"""
SECRET = 6
guess_count = 0
get guess
while guess != SECRET
    guess_count += 1
    if guess < SECRET
        display Higher
    else
        display Lower
    get guess
display guess right
"""
SECRET = 6
guess_count = 0

guess = int(input("Guess a number: "))
while guess != SECRET:
    guess_count += 1
    if guess < SECRET:
        print("Higher")
    else:
        print("Lower")
    guess = int(input("Guess a number: "))
print(f"You got it in {guess_count + 1} guesses!")

# 6. Nested Loops
"""
get row_num,column_num
repeat row_num times
    repeat column_num times
        display number
"""
row_num = int(input("Rows: "))
column_num = int(input("Columns: "))

for i in range(row_num):
    for j in range(column_num):
        print(j, end=" ")
    print()
