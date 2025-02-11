#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:27:42 2025

@author: mikemcrae
"""


#%%
# Import necessary libraries
import pandas as pd

# Define a function
def calculate_mean(numbers):
    """Returns the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

# Top-level script environment
if __name__ == "__main__":
    # Example data
    data = [10, 20, 30, 40, 50]
    
    # Compute mean using the function
    mean_value = calculate_mean(data)
    
    # Print the result
    print(f"The mean of the dataset is: {mean_value}")


#%%

# --- Variables and Data Types ---
x = 10  # Integer
name = "Alice"  # String
pi = 3.14  # Float
is_python_fun = True  # Boolean

print(f"Integer: {x}, String: {name}, Float: {pi}, Boolean: {is_python_fun}")

# --- Data Structures ---
# List (Ordered, Mutable)
my_list = [1, 2, 3]
my_list.append(4)
print(f"List: {my_list}")

# Dictionary (Key-Value Pairs)
my_dict = {"name": "Alice", "age": 25}
print(f"Dictionary: {my_dict}")

# Tuple (Immutable Sequence)
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple}")

# Set (Unordered, Unique Elements)
my_set = {1, 2, 3, 1, 2}  # Duplicates are removed
print(f"Set: {my_set}")

# --- Control Flow ---
# If-elif-else
num = 10
if num > 10:
    print("Greater than 10")
elif num == 10:
    print("Exactly 10")
else:
    print("Less than 10")

# Loops
print("For loop output:")
for i in range(3):
    print(i)

print("While loop output:")
count = 0
while count < 3:
    print(count)
    count += 1

# --- List Comprehensions ---
squares = [x**2 for x in range(10)]
print(f"Squares using list comprehension: {squares}")

# --- Error Handling ---
try:
    x = int("abc")  # This will cause an error
except ValueError:
    print("Invalid input: Cannot convert 'abc' to an integer")


#%% Importing dataframe and mnipulating
import pandas as pd

# Load the CSV file
df = pd.read_csv("student_data.csv")

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Group by Department and calculate the average salary
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(avg_salary)

# Count number of students per department
dept_counts = df["Department"].value_counts()
print("\nNumber of Students per Department:")
print(dept_counts)

# Filter students older than 40
older_students = df[df["Age"] > 40]
print("\nStudents older than 40:")
print(older_students)
