#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95

# Get the test scores.
#needed to convert the inputs from the user to type int as it is currently taking str
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
#adding test3 as it is not declared. We will need it to calculate the average
test3 = int(input('Enter the score for test 3: '))
# Calculate the average test score.
#I added the parenthesis to fix the order of operations logic. The way it was before, test3 was divided by 3
#added to test1 and test2. Now we are adding test1,2, and 3 then dividing by 3. This is logically correct to find the average
average = (test1 + test2 + test3) / 3
# Print the average.
#just adding space and a colon here in the print statement to make it look cleaner
print('The average score is: ', average)
# If the average is a high score,
# congratulate the user.
#the variables declared are case sensitive. We need to make sure that the variable is the same as the variable declared
if average >= HIGH_SCORE:
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

def area_of_rectangle(length, width):
    return length * width

def get_rectangle_dimensions_from_user():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))

    return length, width

print("Enter the dimensions of the first rectangle:")
length1, width1 = get_rectangle_dimensions_from_user()
area_of_rectangle1 = area_of_rectangle(length1, width1)

print("Enter the dimensions of the second rectangle:")
length2, width2 = get_rectangle_dimensions_from_user()
area_of_rectangle2 = area_of_rectangle(length2, width2)

print("The area of the first rectangle is: ", area_of_rectangle1)
print("The area of the second rectangle is: ", area_of_rectangle2)


#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

def user_nae_age_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

name, age = user_nae_age_input()
print("Your name is", name, "and you're ", age, "years old.")


#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

print("Happy birthday, ", name, "! You are ", age, " years old today!")
