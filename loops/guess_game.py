import random 
random_number = random.randint(1, 101)
guess = 0


while True: #boolean to keep the looop running 
    guess_number = int(input("Guess a number: "))
    guess = guess + 1

    #compare now
    if random_number < guess_number:
        print ("Lower")
    elif random_number > guess_number:
        print ("Higher")
    else : 
        print ("You got it right !!!")
        break
print(f"It took you {guess} guesses.")