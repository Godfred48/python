word =  "Commitment" 
letter = input(str("What is your favorite letter?"))

for i in word:
  if i.lower() == letter.lower(): #compare the letter with the letters in the word, ignoring case
    print("_", end="") #end="" means that the next print statement will be printed on the same line
  else:
    print(i.lower(), end="")
