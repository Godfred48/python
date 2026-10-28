sentence = "the cat sat on the mat and the dog sat on the log"
word_list = sentence.split()
word_count = {}
word_lengths = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("="*50)
print(word_count)
print("="*50)

max_word = max(word_count, key=word_count.get)
times = word_count[max_word]

print("="*50)
print(word_count)
print("="*50)
print(f"The most occuring word is '{max_word}' ,Which appeared '{times}' times")
print ("="*50)



