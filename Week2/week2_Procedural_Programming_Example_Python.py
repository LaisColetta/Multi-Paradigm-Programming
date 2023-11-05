#WEEK 2 - PROCEDURAL PROGRAMMING EXAMPLE IN PYTHON
#Student: Lais Coletta
#Tasks:
    # Add a doc string to each function in the procedural program, make sure to document each parameter and the return value. 
    #You can see this has done for get average in Listing 3.

import csv

def get_maximum_value(lst):
    """
    Given a list of numbers as input this function will return the maximum value of the numbers listed.
    
    :param lst: List of numbers.
    :return: The maximum value in the list.
    """
    maximum = lst[0]
    for l in lst:
        if maximum < l:
            maximum = l
    return maximum

def get_minimum_value(lst):
    """
    Given a list of numbers as input this function will return the minimum value of the numbers listed.
    
    :param lst: List of numbers.
    :return: The minimum value in the list.
    """
    minimum = lst[0]
    for l in lst:
        if minimum > l:
            minimum = l
    return minimum

def get_average(lst):
    """
    Given a list of numbers as input this function will return the numerical average .
    : param list : the list of numbers given as input
    : return : the numerical average of the list
    """
    total = 0
    for l in lst:
        total += l
    average = total / len(lst)
    return average

def get_median_value(lst):
    """
    Given a list of numbers as input this function will return the median value of the numbers listed.
    
    :param lst: List of numbers.
    :return: The median value in the list.
    """
    list1 = lst.copy()
    bubble_sort(list1)
    median = list1[len(list1) // 2]
    return median

def bubble_sort(lst):
    """
    Given a list of numbers as input this function will sort a list of elements in ascending order.

    :param lst: A list of elements to be sorted.
    :return: The list in ascending order.
    """
    for i in range(0, len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

def get_mode(lst):
    """
    Get the mode value from a list of numbers.
    
    :param lst: List of numbers.
    :return: The mode value in the list.
    """
    highest_freq = 0
    mode = lst[0]
    for score in lst:
        frequency = 0
        for score2 in lst:
            if score == score2:
                frequency += 1
        if frequency > highest_freq:
            mode = score
            highest_freq = frequency
    return mode

def read_scores_from_csv(filename):
    """
    Read a list of scores from a CSV file.
    
    :param filename: The name of the CSV file.
    :return: List of scores.
    """
    scores = []
    with open(filename, mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            score = int(lines["Score"])
            scores.append(score)
    return scores

if __name__ == "__main__":
    scores = read_scores_from_csv('example.csv')

    average = get_average(scores)
    minimum = get_minimum_value(scores)
    maximum = get_maximum_value(scores)
    median = get_median_value(scores)
    mode = get_mode(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} Mode: {mode}')

#Move the functions around, you should find that this has no effect on the program execution as they
#are just blocks of code which are called by the “main method” at the bottom. This won’t be true in
#older languages like C, so be aware of that.

import csv

if __name__ == "__main__":
    scores = read_scores_from_csv('example.csv')

    average = get_average(scores)
    minimum = get_minimum_value(scores)
    maximum = get_maximum_value(scores)
    median = get_median_value(scores)
    mode = get_mode(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} Mode: {mode}')

def get_maximum_value(lst):
    """
    Given a list of numbers as input this function will return the maximum value of the numbers listed.
    
    :param lst: List of numbers.
    :return: The maximum value in the list.
    """
    maximum = lst[0]
    for l in lst:
        if maximum < l:
            maximum = l
    return maximum

def get_minimum_value(lst):
    """
    Given a list of numbers as input this function will return the minimum value of the numbers listed.
    
    :param lst: List of numbers.
    :return: The minimum value in the list.
    """
    minimum = lst[0]
    for l in lst:
        if minimum > l:
            minimum = l
    return minimum

def get_average(lst):
    """
    Given a list of numbers as input this function will return the numerical average .
    : param list : the list of numbers given as input
    : return : the numerical average of the list
    """
    total = 0
    for l in lst:
        total += l
    average = total / len(lst)
    return average

def get_median_value(lst):
    """
    Given a list of numbers as input this function will return the median value of the numbers listed.
    
    :param lst: List of numbers.
    :return: The median value in the list.
    """
    list1 = lst.copy()
    bubble_sort(list1)
    median = list1[len(list1) // 2]
    return median

def bubble_sort(lst):
    """
    Given a list of numbers as input this function will sort a list of elements in ascending order.

    :param lst: A list of elements to be sorted.
    :return: The list in ascending order.
    """
    for i in range(0, len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

def get_mode(lst):
    """
    Get the mode value from a list of numbers.
    
    :param lst: List of numbers.
    :return: The mode value in the list.
    """
    highest_freq = 0
    mode = lst[0]
    for score in lst:
        frequency = 0
        for score2 in lst:
            if score == score2:
                frequency += 1
        if frequency > highest_freq:
            mode = score
            highest_freq = frequency
    return mode

def read_scores_from_csv(filename):
    """
    Read a list of scores from a CSV file.
    
    :param filename: The name of the CSV file.
    :return: List of scores.
    """
    scores = []
    with open(filename, mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            score = int(lines["Score"])
            scores.append(score)
    return scores

#Move bubblesort into another .py file and use the import keyword to import it into your file for use in
#the median calculation. This will look something like:

from sorting_algorithms import bubble_sort

def get_median_value(lst):
    list1 = lst.copy()
    bubble_sort(list1)
    median = list1[len(list1) // 2]
    return median

# Add in two new functions which extract some statistics from the data. No imports allowed here.
#Reference: https://stackoverflow.com/questions/40930713/how-to-calculate-variance-and-std-without-import

def calculate_variance(lst): #
    """
    Given a list of numbers as input this function will calculate the variance of a list of numbers.

    :param lst: A list of numbers.
    :return: The variance of the list.
    """
    n = len(lst)
    mean = sum(lst) / n

    squared_diff = [(x - mean) ** 2 for x in lst]
    variance = sum(squared_diff) / n
    return variance


def calculate_standard_deviation(lst): #Reference:https://stackoverflow.com/questions/70087607/how-do-i-calculate-standard-deviation-in-python-without-using-numpy
    """
    Given a list of numbers as input this function will return the standard deviation.

    :param lst: A list of numbers.
    :return: The standard deviation of the list.
    """
    n = len(lst)
    mean = sum(lst) / n

    squared_diff = [(x - mean) ** 2 for x in lst]
    variance = sum(squared_diff) / n

    standard_deviation = variance ** 0.5
    return standard_deviation


#Write a new function to bring in data from a separate column in the CSV file, can you do this by
#modifying the existing method to be more generalised? Consider default parameters (this is a language
#feature of Python).
#Reference: https://realpython.com/python-csv/

def read_data_from_csv(filename, column_name="Score"): #adding the column name makes the function more generalized when reading data from various columns in your CSV file.
    data = []
    with open(filename, mode='r') as file:
            csvFile = csv.DictReader(file)
            for row in csvFile:
                if column_name in row:
                    data.append(row[column_name])
    return data

#Replace 4 functions in the procedural program with imports or the use of the standard Python library.
#For example you could replace get minimum value with the min() function for lists which is built into Python.
#References: https://docs.python.org/3/library/functions.html ; https://www.w3schools.com/python/python_ref_functions.asp

minimum = min(scores)
maximum = max(scores)
average = sum(scores) / len(scores)
median = get_median_value(scores)
mode = get_mode(scores)

print(f'Minimum: {minimum} Maximum: {maximum} Average: {average} Median: {median} Mode: {mode}')