"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
x = type(pi)
print(x, pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)

if(i < 50):
    print("variable i is equal to", i, "therefore less than 50")
else:
    print("variable i is equal to", i, "therefore greater than 50")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if(picked_fruit == 'orange'):
    print("Fruit is", picked_fruit, "therefore color is Orange")
elif(picked_fruit == 'strawberry'):
    print("Fruit is", picked_fruit, "therefore color is Red")
else:
    print("Fruit is", picked_fruit, "therefore color is Yellow")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def Multiplies(arg_1, arg_2):
    result = (arg_1 * arg_2)
    return result


# TODO: Now call the function a few times to calculate the following answers
MultResult = Multiplies(12, 96)
print("12 x 96 =", MultResult)

MultResult = Multiplies(48, 17)
print("48 x 17 =", MultResult)

MultResult = Multiplies(196523, 87323)
print("196523 x 87323 =", MultResult)
