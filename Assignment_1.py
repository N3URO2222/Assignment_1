'''
ASSIGNMENT 1:
Module 2: Basic Python Concepts

Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.



num1 = int(input('Enter the 1st number: '))#using int to ensure only integers are allowed
num2 = int(input('Enter the 2nd number: '))
symbol = input('Enter the symbol (+, -, *, /): ')

if symbol == '+':#using if,elif to create the program
    print(num1 + num2)
elif symbol == '-':
    print(num1 - num2)
elif symbol == '*':
    print(num1 * num2)
elif symbol == '/':
    print(num1 / num2)
else:
    print('Invalid symbol')


Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''
name1=input('Enter Your First Name: ')
name2=input('Enter your Second Name: ')
name3 = name1 + " " + name2# using "" for space between the name
print(f'Hello! {name3}, welcome to the python')#using f strings to include variables directly within a string with the use of {}
