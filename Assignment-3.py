# 1 Write a python script to convert a number into str type.
"""Solution
age = 28
print(type(age))
age = str(age)
print(type(age)) """

# 2 Write a python script to print Unicode of the character ‘m’
"""Solution 
print(ord("m"))
print(chr(109))"""

# 3 Write a python script to print character representation of a given unicode 100.
"""Solution 
print(chr(100))"""

# 4 Write a python script to print any number and its binary equivalent
"""Solution 
userInput = int(input("Enter Any Number : "))
print("You Enterd {0}".format(userInput))

userInput = bin(userInput)
print("Binary value of your Number is {0} : ".format(userInput))"""

# 5 Write a python script to print any number and its octal equivalent.
"""Solution
userInput = int(input("Enter Any Number : "))
print("You Enterd {0}".format(userInput))

userInput = oct(userInput)
print("Octal value of your Number is {0} : ".format(userInput))"""

# 6 Write a python script to print any number and its hexadecimal equivalent.
"""Solution
userInput = int(input("Enter Any Number : "))
print("You Enterd {0}".format(userInput))

userInput = hex(userInput)
print("hexadecimal value of your Number is {0} : ".format(userInput))"""

# 7 Write a python script to store binary number 1100101 in a variable and print it in decimal format.
"""Solution
binary_Value = 0b1100101
print(chr(binary_Value))"""

# 8 Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
"""Solution
hex_Number = 0x2F
print(oct(hex_Number))"""

# 9 Write a python script to store an octal number 125 in a variable and print it in binary format.
"""Solution
oct_Number = 0o125
print(bin(oct_Number))"""

# 10 Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.
"""Solution
oct_Number = 0o25
hex_Number = 0x39

print(bin(oct_Number + hex_Number))"""
