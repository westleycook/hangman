# A game of hangman

# import necessary modules
from random import *
from string import *

# define global constants
STRIKES = 6
WORD_LIST = "thousand_english_words.txt"  # name of text file with word list to be imported. Contains 1,000 most commonly used English words; taken from https://gist.github.com/deekayen/4148741

# define main program for game play
def main():
    print("LET'S PLAY!")
    play_game() # defined below
    # when game finishes, allow user to play again as many times as desired without restarting program
    while True:
        again = str(input("Want to play again? Y or N: ")).upper()
        # idiot-proofing
        while not (again == "Y" or again == "N"):
            again = str(input("Sorry, couldn't read that. Please enter Y or N: ")).upper()
        if again == "Y":
            print("\nNEW GAME")
            play_game()
        else:
            break

# define helper funciton to import word list and let user choose length of allowable words
def get_words():
    # import words from text file named above
    with open(WORD_LIST, "r") as infile:
        # create list with all words
        all_words = infile.read().split()
        word_length = ""
        # allow user to choose permissible word length
        print("First, choose allowable word length. Options are 3-5 letters, 6+ letters, or any length")
        word_length = str(input("Please enter your choice: "))
        # idiot-proofing
        while word_length not in ["3-5 letters", "3-5", "any length", "any", "6+ letters", "6+"]:
            word_length = str(input("Whoops! Try again. Permissible options are '3-5', '6+', or 'any': "))
        # use list comprehension to return modified list of words based on their length
        if word_length in ["3-5 letters", "3-5"]:
            return [word for word in all_words if (6 > len(word) > 2)]
        elif word_length in ["6+ letters", "6+"]:
            return [word for word in all_words if len(word) > 5]
        else:
            return all_words

# define helper function for guessing letters
def letter_guess():
    # take user guess
    guess = str (input ("Enter a letter: ")).upper()
    # idiot-proofing
    while len(guess) != 1 or guess not in ascii_uppercase:
        guess = str(input("Whoops! That didn't work. Please enter a single letter from A-Z: ")).upper()
    return guess

# define basic gameplay function
# it's kind of a long function, but I found it tricky to break up because of how the variables interact with each other
def play_game():
    word_list = get_words()
    guesses_left = STRIKES
    # choose random word from imported list to be the answer word
    answer_word = word_list[randint(0, len(word_list) - 1)].upper()
    # initialize other variables
    letters_guessed = []
    progress_word = ""
    guess = ""
    # print underscores for each letter in the answer word to show user how long it is
    print("The word is", end = " ")
    for char in answer_word:
        print("_", end = " ")
    # tell user how many guesses
    print("\nYou have", guesses_left, "guesses.")
    # the core of the game:
    while guesses_left > 0 and progress_word != answer_word:
        # take letter guess
        user_guess = letter_guess()
        # idiot-proofing to ensure the same letter can't be guessed twice
        while user_guess in letters_guessed:
            print("Whoops, you already guessed that one! Try again.")
            user_guess = letter_guess()
        # add user guess to list of already-guessed letters
        letters_guessed += user_guess
        # in case of correct guess
        if user_guess in answer_word:
            print("\nNice! The letter", user_guess, "is in the word.")
        # for incorrect guess
        else:
            print("\nOh no! The letter", user_guess, "is NOT in the word.")
            # print gallows with relevant body parts (function defined below)
            draw_hanging(6 - guesses_left)
            # take away a guess
            guesses_left -= 1
        # re-make progress word incorporating latest user guess
        progress_word = ""
        for char in answer_word:
            if char in letters_guessed:
                progress_word += char
            else:
                progress_word += "_"
        # break loop here if game is over (b/c all steps below are unnecessary)
        if progress_word == answer_word or guesses_left == 0:
            break
        # show user letters guessed incorrectly so far (blank if all guesses are correct)
        print("Letters guessed incorrectly:", end=" ")
        for char in letters_guessed:
            if char not in answer_word:
                print(char, end = " ")
        # show user progress toward guessing the word
        print("\nThe word is:", end = " ")
        # prints already-guessed letters in correct places and underscores elsewhere
        for char in progress_word:
            print(char, end = " ")
        print()
        # tell user how many guesses left, changing "guesses" to "guess" when grammatically necessary
        if guesses_left == 1:
            print("You only have", guesses_left, "guess left!")
        else:
            print("You have", guesses_left, "guesses left.")
    # after the while loop, if user won
    if progress_word == answer_word:
        print("The word was", answer_word)
        print ("YOU WIN!")
    # if user lost
    else:
        print("You lost :(")
        print("The word was", answer_word)

# helper function to draw gallows with relevant body parts
def draw_hanging(step):
    # there's gotta be a smoother way to do this than with separate conditional statements for each one, but this works
    # all drawing helper functions defined below
    if step == 0:
        draw_gallows()
    elif step == 1:
        draw_head()
    elif step == 2:
        draw_arms()
    elif step == 3:
        draw_body()
    elif step == 4:
        draw_leg_1()
    else:
        draw_leg_2()

# define drawing helper functions
# would have been nice to do these with drawingPanel but I ran out of time
# also, making the user jump to a second tab/window to see the display didn't seem cool

# draw just the gallows
def draw_gallows():
    print(" __________")
    print("  \     /  |")
    print("   \   /   |")
    print("    \_/    |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")

# draw gallows with head
def draw_head():
    print(" __________")
    print("  \     /  |")
    print("   \   /   |")
    print("    \_/    |")
    print("    ---    |")
    print("   |   |   |")
    print("    ---    |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")

# draw gallows with head and arms
def draw_arms():
    print(" __________")
    print("  \     /  |")
    print("   \   /   |")
    print("    \_/    |")
    print("    ---    |")
    print("   |   |   |")
    print("    ---    |")
    print("  ___|___  |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")

# draw gallows with head, arms, and body
def draw_body():
    print(" __________")
    print("  \     /  |")
    print("   \   /   |")
    print("    \_/    |")
    print("    ---    |")
    print("   |   |   |")
    print("    ---    |")
    print("  ___|___  |")
    print("     |     |")
    print("     |     |")
    print("           |")
    print("           |")
    print("           |")
    print("           |")

# draw gallows with head, arms, body, and one leg
def draw_leg_1():
    print(" __________")
    print("  \     /  |")
    print("   \   /   |")
    print("    \_/    |")
    print("    ---    |")
    print("   |   |   |")
    print("    ---    |")
    print("  ___|___  |")
    print("     |     |")
    print("     |     |")
    print("    /      |")
    print("   /       |")
    print("           |")
    print("           |")

# draw gallows with full body
def draw_leg_2():
    print(" __________")
    print("  \     /  |")
    print("   \   /   |")
    print("    \_/    |")
    print("    ---    |")
    print("   |   |   |")
    print("    ---    |")
    print("  ___|___  |")
    print("     |     |")
    print("     |     |")
    print("    / \    |")
    print("   /   \   |")
    print("           |")
    print("           |")

# call to main function
main()
