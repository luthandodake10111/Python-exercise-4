#------------------------------------------------------------------------------------
#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.
def check_attendance(students, absentees):
     absent_students = []

     for student in students:
        if student in absentees:
            absent_students.append(student)
            return absent_students

# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.

result = check_attendance(["Alice", "Bob", "Charlie", "David"], ["Bob", "David"])
print(result)
#------------------------------------------------------------------------------------
# Task 2: Function for Real-Life Data Processing

student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}


# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.

def calculate_average_grade(my_dick: dict):
    total_grades = 0

    for key in my_dick:
        total_grades = total_grades + my_dick[key]

    return total_grades /len(my_dick)

# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.

average = calculate_average_grade(student_grades)
print(f"The average is: {average}")


#------------------------------------------------------------------------------------
# Task 3: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.

def operation_selector(operation):
    if operation == "add":
        return lambda x, y: x + y  
    elif operation == "multiply":
        return lambda x, y: x * y 
    else:
        raise ValueError("Invalid operation. Use 'add' or 'multiply'.")

# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.

add_function = operation_selector("add")
result_add = add_function(4, 6)
print(result_add)

# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.

multiply_function = operation_selector("multiply")
result_multiply = multiply_function(3, 7)
print(result_multiply)


#------------------------------------------------------------------------------------
# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.
# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)

def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    total_cost = (distance / fuel_efficiency) * fuel_price
    return total_cost

# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}

# TODO: Use a for loop to print each item and its quantity in stock.

for item, quantity in grocery_inventory.items():
    print(f"{item}: {quantity} in stock")

# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).

total_items = sum(grocery_inventory.values())
print(f"Total number of items in stock: {total_items}")

#------------------------------------------------------------------------------------
# Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

# TODO: Ask the user to input their PIN.
# TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
# TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".

correct_pin = "1234"
attempts = 0
max_attempts = 3

# TODO: Use a while loop to implement the retry system.

while attempts < max_attempts:
    user_input = input("Please enter your PIN: ")
    
    if user_input == correct_pin:
        print("Access Granted")
        break  # Exit the loop if the PIN is correct
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")

if attempts == max_attempts:
    print("Account Locked.")

#------------------------------------------------------------------------------------
# Task 6: Using a for loop with range() for a School Grading System

# TODO: Create a list with 10 random assignment scores (between 0 and 100).
# TODO: Use a for loop to calculate the total score.
# TODO: Calculate and print the average score for the class.
# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.

import random

# List of 10 student scores.
scores = [random.randint(0, 100) for _ in range(10)]

# TODO: Calculate total and average scores.

total_score = 0

for score in scores:
    total_score += score

average_score = total_score / len(scores)

print("Scores:", scores)
print("Total Score:", total_score)
print("Average Score:", average_score)

if average_score > 75:
    print("Congratulations! The class average is above 75.")


#------------------------------------------------------------------------------------
# Task 7: Using the random module (Real-life Scenario: Random Team Selection)

# TODO: Create a list with the names of 20 participants.
# TODO: Use the random module to select 5 random participants.
# TODO: Print the names of the selected team members.

import random

# List of participants.
participants = [
    "Person1", "Person2", "Person3", "Person4", "Person5",
    "Person6", "Person7", "Person8", "Person9", "Person10",
    "Person11", "Person12", "Person13", "Person14", "Person15",
    "Person16", "Person17", "Person18", "Person19", "Person20"
]

# TODO: Randomly select 5 people from the participants list.

selected_team = random.sample(participants, 5)

print("Selected team members:")
for member in selected_team:
    print(member)


#------------------------------------------------------------------------------------
# Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# Step 1: Create a module named 'fitness_tracker.py' with the following functions:
"""
def walk_calories(distance_km):
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    # Calories burned per km cycling: 70
    return distance_km * 70
"""

# Step 9: Use the custom module in your main script:
# TODO: Import the custom 'fitness_tracker' module.
# TODO: Ask the user to input the distance they walked, ran, and cycled today.
# TODO: Calculate and print the total calories burned for each activity.
# TODO: Sum and print the total calories burned for the day.

from fitness_tracker import walk_calories, run_calories, cycle_calories

def main():
    # Ask the user for input
    walking_distance = float(input("Enter the distance you walked today (in km): "))
    running_distance = float(input("Enter the distance you ran today (in km): "))
    cycling_distance = float(input("Enter the distance you cycled today (in km): "))

    # Calculate calories burned for each activity
    calories_walked = walk_calories(walking_distance)
    calories_ran = run_calories(running_distance)
    calories_cycled = cycle_calories(cycling_distance)

    # Print the results
    print(f"Calories burned walking {walking_distance} km: {calories_walked}")
    print(f"Calories burned running {running_distance} km: {calories_ran}")
    print(f"Calories burned cycling {cycling_distance} km: {calories_cycled}")

    # Calculate and print the total calories burned for the day
    total_calories = calories_walked + calories_ran + calories_cycled
    print(f"Total calories burned today: {total_calories}")
#------------------------------------------------------------------------------------
# Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# TODO: Ask the user to input the total loan amount.
# TODO: Ask the user to input their monthly repayment amount.
# TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
# TODO: Print the remaining loan amount after each payment.
# TODO: When the loan is fully paid off, print a congratulatory message.

loan_amount = float(input("Enter the total loan amount: "))
monthly_payment = float(input("Enter your monthly payment amount: "))

# TODO: Use a while loop to simulate the repayment process.

while loan_amount > 0:
    loan_amount -= monthly_payment

if loan_amount > 0:
        print(f"Remaining loan amount: R{loan_amount:.2f}")
else:
        print("Congratulations! Your loan is fully paid off!")