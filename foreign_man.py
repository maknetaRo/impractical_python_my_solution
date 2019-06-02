import pprint
from collections import defaultdict
import sys

sentence = input("Enter a sentence in English: ").lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

d = defaultdict(list)
for char in alphabet:
    d[char] = []
for char in sentence:
    if char in alphabet:
        d[char].append(char)

print("{}\n".format(sentence, file=sys.stderr))
pprint.pprint(d, width=110)

spanish_sentence = input("Enter the same sentence in Spanish: ").lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
d = defaultdict(list)
for char in alphabet:
    d[char] = []

for char in spanish_sentence:
    if char in alphabet:
        d[char].append(char)

print("{}\n".format(spanish_sentence, file=sys.stderr))
pprint.pprint(d, width=110)
