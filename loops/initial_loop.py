#initial loop 
number = -1 

while number < 0:
    number = int(input("Enter a positive number: "))
    if number < 0:
        print("Sorry the number is a negative number .Try again!!!!")
    else:
        print (f"You entered a positive number {number}")