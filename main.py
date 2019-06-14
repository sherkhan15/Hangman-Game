import random
HANGMAN = (
"""
-----
|    |
|
|
|
|
|
|
|
|
|
|
-------
"""
  ,
"""
-----
|   |
|   0
|
|
|
|
|
|
|
|
------
"""
  ,
"""
-----
|   |
|   0 
|   |
|
|
|
|
|
|
|
|
------
"""
  ,
"""
-----
|   |
|   0 
|  /|
|
|
|
|
|
|
|
|
------
"""
  ,
"""
-----
|   |
|   0 
|  /|\
|
|
|
|
|
|
|
|
------
"""
  ,
"""
-----
|   |
|   0 
|  /|\
|  /
|
|
|
|
|
|
|
------
"""
  ,
"""
-----
|   |
|   0 
|  /|\
|  / \
|
|
|
|
|
|
|
------
""")
print(HANGMAN[0])

play_again = True

while play_again:

         words_list = ['abruptly', 'absurd', 'abyss', 'affix']

         chossenword = random.choice(words_list).lower()
         guess = None   #player guess input
         guessed_letters = []   #we add all of the users guesses to this list.
         blank_word = []  #repalcing all the letetrs of the chosen word with dashed symbol.
for letter in chossenword:
    blank_word.append('-')
attempt = 6

while attempt > 0:

        if (attempt!= 0 and "-" in blank_word):

            print(('\n You Have () attempts remaining.').format(attempt))

        try:
            guess == str(input('\n please select a letter between A_Z')).lower()
        except :
            print("that's not a valid input , please try again.")
            continue

        else:
            if not guess.isaplha():
                print('that is not a letter, please try again ')
                continue

            elif len(guess) > 1:
             print("that's is more than one letter, please try again")
             continue

            elif guess in guessed_letters:
                print(" you have already guessed that letter , please try again.")
                continue
            else:
                pass

            guessed_letters.append(guess)

            if guess not in chossenword:
                attempt = -1
                print(HANGMAN[(len(HANGMAN)-1)-attempt])

            else:
                SearchMore = True
                startsearchindex == 0
                while searchMore:
                    try:
                        foundAtIndex = chossenword.index(guess, startsearchindex)
                        blank_word[foundAtIndex] = guess
                        startsearchindex = foundAtIndex + 1
                    except:
                        searchMore = False

            print("".join(blank_word))

            if attempt == 0:
                print("sorry. the game is over , The word was" + chossenword)
                print("\nWould you like to play again ?")
                response = input('>').lower()
                if response not in ("yes", "y"):
                    play_again = False
                    print("thanks for playing HANGMAN!")
                break

            if "-" not in blank_word :
                print((" \n  Congratualtion! {} was the word ").format(chossenword))
                print("\n World you like to play again ?")
                response = input('>').lower()
                if response not in ("yes", "y"):
                    play_again = False
                    print("thanks for playing HANGMAN!")
                break








