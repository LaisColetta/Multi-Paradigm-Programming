#MPP - Week 1 - Programming Exercise
#STUDENT: Lais Coletta Pereira 

#Do the following in Python:
#1- Write a program that asks the user for their name and greets them with their name:

username = input("Please add your name ")

print("Hi, "+ username)

#• Modify the previous program such that only the users Alice and Bob are greeted with their names.

username = input("Please add your name ")

if username == "Alice" or username == "Bob":
    print("Hi, " + username)
else:
    print("Please insert Alice or Bob to be greeted")

#• Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
n = int(input ("This program will print the sum of the numbers 1 to n. Please, insert a positive number: "))

#create variable for the for loop (to repeat the sum of the numbers from 1 to n)
numb = 0
#Calculate the sum of numbers from 1 to n

for i in range (1, n + 1):
    numb +=i

print(numb)

#• Modify the previous program such that only multiples of three or five are considered in the sum, e.g.
#3, 5, 6, 9, 10, 12, 15 for n=17
# If I understood the question correctly, we should use a loop to calculate the sum of numbers that are multiples of 3 or 5 until the variable n value. 
n = int(input ("This program will print the sum of the numbers 1 to n that are multiples of 3 or 5. Please, insert a positive number: "))

for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            numb += i

print("The sum of multiples of 3 or 5 to ", n, " value is:", numb)

#• Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,. . . ,n.
## Ask the user for a number n
n = int(input("This program will give you the option to calculate the SUM or PRODUCT of a given number. Please insert a positive number: "))

# Ask the user to choose between sum and product
calculation_type = input("Please select 'SUM' or 'PRODUCT' of numbers from 1 to n: ")

# Check if the input is valid
if calculation_type == "SUM":
    # Calculate the sum of numbers from 1 to n
    sum_of_numbers = sum(range(1, n + 1))
    print("The SUM of the numbers from 1 to", n, "is:", sum_of_numbers)
elif calculation_type == "PRODUCT":
    product = 1
    for i in range(1, n + 1):
        # Calculate the product
        product *= i
    print("The PRODUCT of numbers from 1 to", n, "is:", product)
else:
    print("Please select 'SUM' for sum or 'PRODUCT' for product")


#• Write a program that prints a multiplication table for numbers up to 12. (References: https://www.javatpoint.com/python-display-multiplication-table & https://www.educative.io/answers/how-to-create-a-multiplication-table-for-any-number-in-python)
# Define the variable range number up to 12
max_number = 12
print("This is a multiplication table up to the number 12:")

# Print the column headers
print("   |", end="")
for i in range(1, max_number + 1):
    print(f"{i:4}", end="")
print("\n" + "-" * 49)

# Print the multiplication table
# References: https://www.toppr.com/guides/python-guide/examples/python-examples/decision-making-and-loops/multiplication-table/python-program-to-display-the-multiplication-table/
for i in range(1, max_number + 1):
    print(f"{i:2} |", end="")
    for j in range(1, max_number + 1):
        result = i * j
        print(f"{result:4}", end="")
    print()

#• Write a program that prints all prime numbers smaller than 100.
# Reference: https://www.javatpoint.com/program-to-print-all-prime-numbers-between-1-to-100
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

# Print prime numbers smaller than 100
print("Prime numbers smaller than 100:")
for num in range(2, 100):
    if is_prime(num):
        print(num, end=" ")

print()

#Zip up these programs and submit the zip file on Moodle. Reference: https://www.tutorialspoint.com/How-to-create-a-zip-file-using-Python
import zipfile
file = 'MPP - Week 1 - Programming Exercise.py'
Week1_Programming_Exercise = 'MPP_Week1_Programming Exercise.zip'
with zipfile.ZipFile(Week1_Programming_Exercise, 'w') as zipf:
    zipf.write(file)

print(f'Zip archive "{Week1_Programming_Exercise}" created successfully.')
