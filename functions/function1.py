def display_regular(value):
    return value

def display_upperCae(value):
    return value.upper()

def display_lowerCase(value):
    return value.lower()

user_input = (input("Enter anything in mind: "))
while True:
    if not user_input.isdigit():
        print(display_regular(user_input))
        print(display_upperCae(user_input))
        print(display_lowerCase(user_input))
        break
    else:
        print("You Entered a number, please enter something else.")
        user_input = (input("Enter anything in mind: "))
