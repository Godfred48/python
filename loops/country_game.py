word = "korea"
guesses = 0
output = "_ " * len(word)

print ("Welcome to the country guessing game!")
print (f"Your hint is: {output}")

while True: 
    user_input = input("What is your guess? ")


    if len(user_input) != len(word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else :
        output = ""
        for i in range(len(word)) :
            if word[i].lower() == user_input[i].lower():
                output += word[i].upper() + " "
            else:
                output += "_ "
        guesses += 1   #guesing correct values length only

        print(f"Your hint is {output}")

        if "_" not in output:
            print ("congratulations you guessed the right country")
            print( f"Your guesses attempt was {guesses} ")
            break



        


