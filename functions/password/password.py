#Password strength checker
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]


""" function reads the wordss in nthe file and compares with the word user enters"""
def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r",encoding="utf-8") as file: #encoding="utf-8" helps python reads file properly 
        for line in file:
            line_word = line.strip()
            if case_sensitive:
                if word == line_word:
                    return True
            else:
                if word.lower() == line_word.lower():
                    return True
        return False 

"""function checks if each word is present in the main word list"""
def word_has_character(word, character_list):
    for i in range(len(word)):
        if word[i] in character_list:
            return True
    return False 

"""function checks for word complexity based on length and character types"""
def check_word_complexity(word):
    complexity_score = 0
    lowercase = word_has_character(word, LOWER)
    uppercase = word_has_character(word, UPPER)
    digits= word_has_character(word, DIGITS)
    special = word_has_character(word, SPECIAL)

    if lowercase:
        complexity_score += 1
    if uppercase:
        complexity_score += 1
    if digits:
        complexity_score += 1
    if special:
        complexity_score += 1
    return complexity_score

"""checking password strength based on complexity and length"""
def password_strength(password, min_length=10, strong_lenght=16):
    complexity = check_word_complexity(password)
    if len(password) < min_length:
        complexity += 0
    else : 
        if len(password) > min_length and len(password) >= strong_lenght:
            complexity += 1
    strength = complexity
    return strength

def main():
    while True:
        print("=" * 50)
        password = input("Enter a password to check its strength: ")
        print("=" * 50)
        if password == "q" or password == "Q":
            print("Exiting the password strength checker.")
            print("-" * 50)
            print("Thank you for using the password strength checker. Later!")
            break
        else :
            toppassword = word_in_file(password, "toppasswords.txt")
            wordlist = word_in_file(password, "wordlist.txt")
            if toppassword == True:
                print("This password is too common. Please choose a different one.")
            elif wordlist == True:
                print("This password is a dictionary word. Please choose a different one.")
            else:
                strength = password_strength(password)
                if strength < 3:
                    print(f"This password score is {strength} (Weak). Please choose a different one.")
                elif strength == 3:
                    print(f"This password score is {strength} (Moderate). Consider making it stronger.")
                else:
                    print(f"This password score is {strength} (Strong).")


if __name__ == "__main__":
    main()