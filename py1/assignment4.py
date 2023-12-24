"""
Author: ye wente
Assignment / Part: HW1 - Q4
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Bornforthis 1v1 School of Computer Science and Procedures on
Academic Misconduct.
"""

print("Please enter your amount of dollars and cents, in two separate lines.")
dollars = float(input())
cents = float(input())
total = dollars + cents/100
quarters = int(total//0.25)
dimes = (total % 0.25)//0.1
nickels = (total % 0.25 % 0.1)//0.05
pennies = (total % 0.25 % 0.1 % 0.05)//0.01


print(str(dollars) + " dollars and " + str(cents) + " cents are: " + str(quarters) + " quarters, " + str(dimes) + " dimes, " + str(nickels) + " nickels and " + str(pennies) + " pennies")


