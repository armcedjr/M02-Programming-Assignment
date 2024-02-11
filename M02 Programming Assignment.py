# -*- coding: utf-8 -*-
"""
Armando Cedano
M02 Programming Assignment
This code is the answers to the 4.1, 4.2 and 6.1 to 6.3 of Things To Do questions.
"""

# 4.1
# Choose a number between 1 and 10 and assign it to the variable secret.
# Then, select another number between 1 and 10 and assign it to the variable guess.
# Next, write the conditional tests (if, else, and elif) to print the string 'too low'
# if guess is less than secret, 'too high' if greater than secret, and 'just right' if equal to secret.
secret = 7
guess = 5

if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')

# 4.2
# Assign True or False to the variables small and green.
# Write some if/else statements to print which of these matches those choices: cherry, pea, watermelon, pumpkin.
small = True
green = False

if small and green:
    print("pea")
elif small and not green:
    print("cherry")
elif not small and green:
    print("watermelon")
else:
    print("pumpkin")

# 6.1
# Use a for loop to print the values of the list [3, 2, 1, 0].
for i in [3, 2, 1, 0]:
    print(i)

# 6.2
# Assign the value 7 to the variable guess_me, and the value 1 to the variable number.
# Write a while loop that compares number with guess_me.
# Print 'too low' if number is less than guess_me.
# If number equals guess_me, print 'found it!' and then exit the loop.
# If number is greater than guess_me, print 'oops' and then exit the loop.
# Increment number at the end of the loop.
guess_me = 7
number = 1

while number <= guess_me:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    number += 1

# 6.3
# Assign the value 5 to the variable guess_me.
# Use a for loop to iterate a variable called number over range(10).
# If number is less than guess_me, print 'too low'.
# If it equals guess_me, print found it! and then break out of the for loop.
# If number is greater than guess_me, print 'oops' and then exit the loop.
guess_me = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
