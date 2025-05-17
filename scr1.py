input_string = input("слова: ")
words = []
current_word = []
for char in input_string.lower():
    if char.isalpha():
        current_word.append(char)
    else:
        if current_word:
            words.append(''.join(current_word))
            current_word = []
if current_word:
    words.append(''.join(current_word))
unique_words = sorted(set(words))
print("Слова в порядке:")
for word in unique_words:
    print(word)