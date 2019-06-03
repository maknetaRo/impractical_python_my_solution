# Load digital dictionary file as a list of words
# Create empty list to hold palindromes
# Loop through each word in the word list:
# Iword sliced forward is the same as word sliced backward:
# append word to palindrome list
# Print palindrome list
import load_dictionary

word_list = load_dictionary.load('2of12.txt')

palindromes = []
for word in word_list:
    if word == word[::-1] and len(word) > 1:
        palindromes.append(word)

print(palindromes)
print("\nNumber of palindormes found = {}\n".format(len(palindromes)))
print(*palindromes, sep=', ')






