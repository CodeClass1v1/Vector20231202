"""
Author: ye wente
Assignment / Part: HW1 - Q3
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Bornforthis 1v1 School of Computer Science and Procedures on
Academic Misconduct.
"""
print("Please enter number of coins:")
quarters = input("Number of quarters: ")
dimes = input("Number of dimes: ")
nickels = input("Number of nickels: ")
pennies = input("Number of pennies: ")
total = int(quarters)*0.25 + int(dimes)*0.1 + int(nickels)*0.05 + int(pennies)*0.01
cents = (total- int(total))*100

print("The total is " + str(int(total) // 1) + " dollar(s) and "+str(round(cents)) + " cent(s)")
