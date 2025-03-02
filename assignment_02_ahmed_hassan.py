# Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])

#returns empty list


# Can you debug and fix the output? The code should return the entire list

print(numbers[0:])
#output [1,2,3,4,5]

# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

def sales_for_the_week():
    sales_for_the_week = []
    for day in range(1, 8):
        try:
            sales = float(input(f"Enter daily sale for day {day}: "))
            sales_for_the_week.append(sales)
        except ValueError:
            print("Invalid input expected numerical value")
    total_sales = sum(sales_for_the_week)
    return total_sales

total_sales = sales_for_the_week()
print(f"Total Sales for the week is {total_sales:.2f}")

# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
# ● Print your list in its original order.
# ● Use the sort() function to arrange your list in order and reprint your list.
# ● Use the sort(reverse=True) and reprint your list.


def sort_locations():
    places_to_visit = ["Egypt", "Japan", "Saudia Arabia", "Bengladesh", "UK"]
    print(f"Places to visit in original order: {places_to_visit}")
    print(f"Sorted list of places to visit:  {sorted(places_to_visit)}")
    print(f"Reverse Sorted list of places to visit:  {sorted(places_to_visit, reverse=True)}")

sort_locations()

# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

courses = {'DATA601': {'room_number': '100', 'instructor': 'Mason Jones', 'meeting_time': '1pm', 'day':'Monday'},
           'DATA602': {'room_number': '101', 'instructor': 'Olivia Davis', 'meeting_time': '2pm', 'day':'Tuesday'},
           'DATA603': {'room_number': '102', 'instructor': 'Noah Smith', 'meeting_time': '3pm', 'day':'Wednesday'},
           'DATA604': {'room_number': '103', 'instructor': 'Emma Williams', 'meeting_time': '4pm', 'day':'Thursday'},
           'DATA605': {'room_number': '104', 'instructor': 'Liam Brown', 'meeting_time': '5pm', 'day':'Friday'},
           'DATA606': {'room_number': '105', 'instructor': 'Ava Garcia', 'meeting_time': '6pm', 'day':'Monday'}
}

def user_enters_course_num():
    while True:
        user_input = input("Enter course Number...")
        if user_input in courses.keys():
            return user_input
        else:
            print("Error not a valid course..")

def display_course_values():
    course = user_enters_course_num()
    print(f"Student selected {course} with instructor {courses[course]['instructor']}. "
          f"The room number is {courses[course]['room_number']}. The meeting time for this course is on "
          f"{courses[course]['day']} at {courses[course]['meeting_time']}")

display_course_values()


# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.

def display_menu():
    print("\nContact Management System")
    print("1. Look up an email address")
    print("2. Add a new contact")
    print("3. Change an existing email")
    print("4. Delete a contact")
    print("5. Exit")

def look_up_email(contacts):
    name = input("Enter the name to look up: ").strip().title()
    if name in contacts:
        print(f"{name}'s Email: {contacts[name]}")
    else:
        print("Name not found.")

def add_contact(contacts):
    name = input("Enter the name: ").strip().title()
    if name in contacts:
        print("This contact already exists!")
    else:
        email = input("Enter the email address: ").strip()
        contacts[name] = email
        print(f"{name} has been added.")

def change_email(contacts):
    name = input("Enter the name whose email you want to change: ").strip().title()
    if name in contacts:
        email = input("Enter the new email address: ").strip()
        contacts[name] = email
        print(f"{name}'s email has been updated.")
    else:
        print("Name not found.")

def delete_contact(contacts):
    name = input("Enter the name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted.")
    else:
        print("Name not found.")

contacts = {}

while True:
    display_menu()
    choice = input("Choose an option (1-5): ").strip()

    if choice == '1':
        look_up_email(contacts)
    elif choice == '2':
        add_contact(contacts)
    elif choice == '3':
        change_email(contacts)
    elif choice == '4':
        delete_contact(contacts)
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

