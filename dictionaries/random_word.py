import random

def main():
    # Create a list that starts with a few numbers.
    words = ["goat", "rat"]
    print(f"Starting list: {words}")
 
    # Call with one argument: quantity uses its default value of 1.
    append_random_words(words)
    print(f"After appending 1 word: {words}")
 
    # Call with two arguments: append 3 random numbers.
    append_random_words(words, 3)
    print(f"After appending 3 more words: {words}")
 
def append_random_words(word_list, quantity=1):
    choice_word = ["apple", "river", "cloud", "stone", "tiger"]
    for _ in range(quantity):
        word = random.choice(choice_word)
        word_list.append(word)

# Call main to start this program.
if __name__ == "__main__":
    main()
