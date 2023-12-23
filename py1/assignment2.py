"""
Author: ye wente
Assignment / Part: HW1 - Q2
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Bornforthis 1v1 School of Computer Science and Procedures on
Academic Misconduct.
"""
year = input("Please enter a year greater than 2023: ")
population= 330109174
birth_year = 86400/7 *365
death_year = -86400/15 *365
immigrant_year = 86400/42 *365
emigration_year = -86400/75 *365
approximate_pop = population + ((int(year)-2023)*(birth_year + death_year +immigrant_year +emigration_year))
print("The population in year " + str(year) + " is: " + str(round(approximate_pop)))