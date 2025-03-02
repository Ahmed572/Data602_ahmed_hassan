# 1. Create a list called animals that contain the following: cat, dog, manta ray, horse, crouching tiger

animals = ["cat", "dog", "manta ray", "horse", "crouching tiger"]

# 2. Repeat question 1 and loop through and print each item in the animal list by iterating through an index number and using range(). Set a variable len_animals to the length of the animal list.

for i in range(len(animals)):
    print(animals[i])


# 3. Programmatically reorganize the countdown list below in descending order and return the value of the 5th element in the sorted countdown list.
#     The 5th element will be stored in the variable the_fifth_element, which currently below has a dummy value of -999.
#     Remember, the index number of the 5th element is not 5
# countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
# the_fifth_element = -999

countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]

countdown.sort(reverse=True)

the_fifth_element = countdown[4]

print("The 5th element in the is: ", the_fifth_element)


# 4. Write a program to add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#Expected output:
#[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# 5. Write a program to remove all occurrences of item 20 in the following list.
# list2 = [5, 20, 30, 15, 20, 30, 20]

list2 = [5, 20, 30, 15, 20, 30, 20]
list2 = [item for item in list2 if item != 20]
print(list2)

# 6. Using the following dictionary .. (Use python to solve for the answer.)
# dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}
# a. What is the name of the course?
# b. Change the course to DATA602
# c. Add new information to the dictionary - "Professor" with "Schettini"
# d. Using the len function, find how many keys there are in the dictionary.

dict_info = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}

# a. What is the name of the course?
print("Course name:", dict_info["Course"])

# b. Change the course to DATA602
dict_info["Course"] = "DATA602"
print(dict_info["Course"])

# c. Add new information - "Professor": "Schettini"
dict_info["Professor"] = "Schettini"
print(dict_info["Professor"])

# d. Find how many keys are in the dictionary
print("Number of keys:", len(dict_info.keys()))


# 7.  Write a Python program to change Brad’s salary to 7500 in the following dictionary.
# sample_dict = {
#     'emp1': {'name': 'Amanda', 'salary': 8200},
#     'emp2': {'name': 'John', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 700}
# }

sample_dict = {
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
}

sample_dict['emp3']['salary'] = 7500
print(sample_dict['emp3']['salary'])





# 1. Write a function to calculate the area and perimeter of a rectangle.

def area_perimiter_rectangle(length, width):
    area = length * width
    perimiter = 2 * (length +  width)

    return area, perimiter




# 2. Write a function to check if a number is even or not.  The function should indicate to the user even or odd.

def even_or_odd(num):
        return f'{num} is even' if num % 2 == 0 else f'{num} is odd'

# 3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample string: “CUNY sps”
# # of upper case characters: 4
# # of lower case characters: 3

def count_case_letters(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())

    return f'# of upper case characters: {upper_count}\n# of lower case characters: {lower_count}'

print(count_case_letters("CUNY sps"))

# 4. Write a Python function to sum all the numbers in a list

def sum_of_list(my_list):
    total = 0
    for num in my_list:
        total += num

    return total

print(sum_of_list([1,2,3,4,5]))

# using built in python sum function

def sum_on_list2(my_list):
    return sum(my_list)

# 5. Create a function that shows an example of global vs local variables.

var = "global"

def local_var():
    var = "local"
    return f"My local variable is {var}"

print(local_var())
print(f"My global variable is {var}")


# 6. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

def multiply_by_unknown(unknown_number):
    def multiplier(x):
        return x * unknown_number
    return multiplier

times_5 = multiply_by_unknown(5)
print(times_5(10))


# You must start a thread before you can read and reply to other threads

