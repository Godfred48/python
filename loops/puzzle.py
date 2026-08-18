# Puzzle Game
word = "love"
no_of_guesses = 0
revealed = "_ " * len(word)

print("Welcome to the word guessing game!")
print("Your hint is:", revealed)

while True:
    input_word = input("What is your guess? ")
    no_of_guesses += 1

    if len(input_word) != len(word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        revealed = ""
        for i in range(len(word)):
            if word[i].lower() == input_word[i].lower():
                revealed += word[i].upper() + " "
            else:
                revealed += "_ "

        print("Your hint is:", revealed)

        if "_" not in revealed:
            print(f"Congratulations! You guessed it! It took you {no_of_guesses} guesses.")
            break