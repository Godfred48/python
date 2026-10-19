"""When finding or retrieving inndividual value for 
   a dictionary, this method is used. Check out third_dict.py to understand 
    how to generate entire value from a dictionary"""

students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
        }

#to geet the value of a divtionary.... create an instance 
 # These are the indexes of the elements in the value lists.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
EMAIL_INDEX = 2
CREDITS_INDEX = 3

#this method is used when finding individual vaalue from a dictionary

id = input("Enter student ID: ")

if id in students_dict:
    value = students_dict[id]
    first_name = value[GIVEN_NAME_INDEX]
    last_name = value[SURNAME_INDEX]
    print(f"{last_name} {first_name}")
else:
    print("No Student Found!")

