students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }

#add an item to the dictionary
students_dict["42-333-4567"] = "Godfred Agbogah"
students_dict["70-300-1000"] = "Taylor Bills"

#remove item from dictionary
students_dict.pop("70-300-1000")
students_dict.pop("42-333-4567")

#finding the length for the dictionary
length = len(students_dict)
print(f"The length for the dictionary is {length}")
print(students_dict)

id = input("Enter the student ID: ")
if id in students_dict:
    name = students_dict[id]
    print(name)
else :
    print("No student found")