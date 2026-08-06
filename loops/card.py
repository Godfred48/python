import random 

play_again = True

while play_again:
    random_card = random.randint(1, 13)
    guess = 0
    print("I'm thinking of a card value between \n 1 and  13. Try to guess it!")

    while True:
        guess_card = int(input("Enter your guess!"))
        guess = guess + 1

        if random_card < guess_card :
            print("Nope, the card is lower!")
        elif random_card > guess_card :
            print("Nope, the card is higher!")
        else:
            break
    print (f"You got it right! It took you {guess} guesses.")

    again = str(input("Would you like to play again? "))
    if again.lower() == "yes":
        play_again = True
    else :
        play_again = False
        print("Goodbye!")




