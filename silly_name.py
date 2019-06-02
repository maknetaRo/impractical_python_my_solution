import random, sys

print("Welcome to the Random Silly Name Picker.\n")

# Load a list of first names
first = ("Baby Oil", "Bad News", "Big Burps", "Bill 'Beenie-Weenie'", "Bob 'Stinkbug'", "Bowel Noises",
              'Boxelder', "Bud 'Lite", "Butternbean", "Buttermilk", "Buttocks", "Chad", "Chesterfield",
              "Chewy","Chigger" "Cinnabuns", "Cleet", "Cornbread", "Crab Meat", "Crapps", "Dark Skies",
              "Dennis Clawhammer", "Dicman", "Elphonso", "Fancypants", "Figgs", "Foncy", "Gootsy",
              "Greasy Jim", "Huckleberry", "Huggy", "Ignatious", "Jimbo", "Joe 'Pottin Soil'",
              "Johnny", "Lemongrass", "Lil Debil", "Longbranch", "Lunch Money", "Mergatroid", '"Mr Peobody"',
              "Oil-Can", "Oinks", "Old Scratch", "Ovaltine", "Pennywhistle", "Pitchfork Ben",
              'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
              "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
              'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
              'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
              "Winston 'Jazz Hands'", 'Worms')
# Load a list of surnames
last = ("Appleyard", "Bigmeat", "Bloominshine", "Boogerbottom", "Breedslovetrout", "Butterbaugh",
             'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
             'Goodensmith','Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater','Hootkins',
             'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
             'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck',
             'Overturf', 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton',
             'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider',
             'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
             'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey',
             'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

while True:
    # Choose a first name at random
    # Assign the name to a variable
    first_name = random.choice(first)
    # Choose a surname at random
    # Assign the name to a variable
    last_name = random.choice(last)
    # Print the names to the screen in order and red font
    print(f"{first_name}  {last_name}", file=sys.stderr)
    # Ask the user to quit or play again

    play_again = input("Would you play again? y/n")
    # If user palys again:
    #     repeat
    if play_again.lower() != 'y':
        break


input("Press Enter to exit.")
