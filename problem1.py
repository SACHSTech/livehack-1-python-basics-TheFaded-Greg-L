'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	Converts Celsius to Fahrenheit

Author:	Lui.G

Created:	07/12/2020
------------------------------------------------------------------------------
'''
# State What The Program Is When Runned (Just Cause)
print("*----| Celsius To Fahrenheit Calculator |----*")
print("")

# Ask User for Celsius 
celsius = float(input("What is the Temperature in Celsius? "))


# F = (9/5 * C) + 32
# Calculate Fahrenheit using C to F Formula
fahrenheit = (9/5 * celsius) + 32

# Output Temperature in Fahrenheit
print("")
print("|---------------------------------------------------|")
print (" Today it is", str(fahrenheit) + "° fahrenheit. Be Careful Out There!")
print("|---------------------------------------------------|")