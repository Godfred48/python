"""sentence = "the cat sat on the mat and the dog sat on the log"
Tasks:

Create a dictionary word_count where each key is a word and each value is how many times it appears.
Print the word that appears most often and how many times.
Create a new dictionary repeated that contains only the words that appear more than once.
Create a dictionary word_lengths that maps each word to its length (each word only once).
Add a new word, "bird", to word_count with a count of 1. Then remove "mat" from it."""

sentence = "the cat sat on the mat and the dog sat on the log"
word_list = sentence.split()
word_count = {}
word_lengths = {}
repeated = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


max_word = max(word_count, key=word_count.get)
times = word_count[max_word]

#repeated words 
for word, count in word_count.items():
    if count > 1:
        repeated[word] = count

#word pe length
for key, value in word_count.items():
    length = len(key)
    word_lengths[key]=length

#adding a new value 
word_count["bird"] = 1
word_count.pop("mat")

print("="*50)
print(word_count)
print("="*50)
print(repeated)
print("="*50)
print(word_lengths)
print("="*50)
print(f"The most occured word is '{max_word}' ,Which appeared {times} times")
print ("="*50)




