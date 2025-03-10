# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.

print("QUESTION 1...")

def meal_recommendation():
    meal = input("Enter a meal (breakfast, lunch, or dinner): ").strip().lower()

    if meal == "breakfast":
        print("How about some bacon and eggs?")
    elif meal == "lunch":
        print("How about a slice of pizza?")
    elif meal == "dinner":
        print("How about chicken over rice and small salad on the side?")
    else:
        print("Sorry, I can only recommend meals for breakfast, lunch, or dinner...")

# Run the function
meal_recommendation()


# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay,
# including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their
# regular hourly pay rate for all hours over 20.
# You should take in the user’s input for the number of hours worked, and their rate of pay.

print("QUESTION 2...")
def payroll(hours, hourly_rate):
    if hours <= 20:
        return hours * hourly_rate
    else:
        non_over_time_compensation = 20 * hourly_rate
        over_time = hours - 20
        over_time_rate = hourly_rate * 1.5
        return (over_time * over_time_rate) + non_over_time_compensation

hourly_rate = float(input("Enter your hourly rate: "))
total_hours_worked = float(input("Enter total hours worked: "))

print("Total compensation for the week: ", payroll(total_hours_worked, hourly_rate))

# Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
print("QUESTION 3...")
def multiple_of_ten(num):
    try:
        return float(num) * 10
    except ValueError:
        return "Error: Please provide a valid number."
    except TypeError:
        return "Error: Input must be a number."

print(multiple_of_ten(5))
print(multiple_of_ten(10))
print(multiple_of_ten(2.2))
print(multiple_of_ten(2.4334))
print(multiple_of_ten("Hello"))

# SQ4: Find the errors, debug the program, and then execute to show the output.
print("QUESTION 4...")
# Code before
# def main()
#       Calories1 = input( "How many calories are in the first food?")
#       Calories2 = input( "How many calories are in the first food?")
#       showCalories(calories1, calories2)
#
# def showCalories()
#    print(“The total calories you ate today”, format(calories1 + calories2,.2f))

# Code After
# Had to add the colons to each function
# moved the show Calories function above the main function
# had to call the main function main()
# fixed case sensitive variables in main function
# had to pass in the calories variables to the showcalories function
# fixed print statement
# added space in the input function for user to enter a readable argument

def showCalories(calories1, calories2):
   print("The total calories you ate today: ", float(calories1) + float(calories2))

def main():
      Calories1 = input( "How many calories are in the first food? ")
      Calories2 = input( "How many calories are in the first food? ")
      showCalories(Calories1, Calories2)

main()

# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#          1/30 + 2/29 + 3/28 ............. + 30/1

print("QUESTION 5...")
def calculate_total():
    total = 0
    for i in range(1, 31):
        total += i / (31 - i)
    return total


result = calculate_total()
print(f"Total of the series: {result:.5f}")


# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT
print("QUESTION 6...")
def triangle_area(base, height):
    try:
        return .5 * (base * height)
    except ValueError:
        return "Error: Please provide a valid number."
    except TypeError:
        return "Error: Input must be a number."

# For example, if the base was 5 and the height was 4, the area would be 10.
print(triangle_area(5, 4))   # should print 10
