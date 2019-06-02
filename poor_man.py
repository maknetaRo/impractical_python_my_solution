import pprint
from collections import defaultdict
import sys

# Take a sentence as input
# assign it to variable
sentence = input("Please enter a text: ")
# assign all the letters to variable alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# use defaultdict from collections to build dictionary keys
d = defaultdict(list)
# iterate through the sentence to lower every letter of in the sentence
for char in sentence:
    char = char.lower()
    # check if the letter (character) is in the alphabet
    if char in alphabet:
        # now add list of letters as a value to each key.
        d[char].append(char)
        
print(sentence)
print("{}\n".format(sentence), file=sys.stderr)
pprint.pprint(d, width=110)


