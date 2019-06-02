# Take an English word
# if word starts with consonant:
#     move the consonant to the end
#     add -ay to the end of the word
# if word starts with vowel:
#     add way to the end of the word

print("Welcome to Pig Latin word game")
while True:
    word = input("Enter an English word: ")
    if word[0] in 'aeiou':
        word = word +'way'
        print(word)
    else:
        word = word[1:] + word[0] + 'ay'
        print(word)
    play_again = input("Would you like to play again? y/n")
    if play_again != 'y':
        break
input("Press Enter to finish the game.")