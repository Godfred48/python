#Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.
print()
print("=" * 50)
age = int(input("Please enter your age: " ))
next_birthday_age = age + 1
print(f"On your next birthday, you will be {str(next_birthday_age)} years old.")

print()
print("=" * 50)

#Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.
carton = int(input("How many egg cartons do you have? "))
eggs_per_carton = 12
total_eggs = carton * eggs_per_carton
print(f"You have {str(total_eggs)} eggs in total.")

print()
print("=" * 50)
#Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.
people = int(input("How many people are here: "))
cookies = int(input("How many cookies do you have: "))
actual = cookies/people 
print(f"Each person wwill get {str(actual)} cookies.")
