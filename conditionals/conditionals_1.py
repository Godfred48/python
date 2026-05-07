#comparing numbers and strings 
first_number = int(input("What is the first nuumber? "))
second_number = int(input("What is the second number? "))

#comparing numbers 
if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")
if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

print("=" * 50)

#comparing string 
fav_animal = "Puppy"
userFav_animal = input("What is your favorite animal? ")
if userFav_animal.capitalize() == fav_animal:
    print("Thats my favorite animal too!")
else:
    print("That is not my favorite animal.")

print("=" * 50)

