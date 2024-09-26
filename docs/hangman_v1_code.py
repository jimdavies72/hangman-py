def hangman(num_guesses, game_phrase, game_word_count, game_clue):
    # Initialisation phase
    print("\n" * 10)

    if game_word_count > 1:
        single_plural = "There are:\t\t\t"
        word_words = " words.\n"
    else:
        single_plural = "There is:\t\t\t"
        word_words = " word.\n"

    if num_guesses == 1:
        num_guess_text = " guess.\n"
    else:
        num_guess_text = " guesses.\n"
    start_text: str = single_plural + str(game_word_count) + word_words + "You have:\t\t\t" + \
                      str(num_guesses) + num_guess_text

    if len(game_clue) > 0:
        start_text = start_text + "The clue is:\t\t" + str(game_clue.capitalize()) + ".\n"

    # create an array of letters from the game phrase provided by the player
    phrase_array: list = []
    for index in game_phrase:
        phrase_array.append(index.upper())

    # clone list array so we can monitor game status later
    guessed_array: list = list(phrase_array)
    # remove spaces as these are not guessed within the game
    for index in guessed_array:
        if index == " ":
            guessed_array.remove(index)

    # create an array of how the game phrase will be displayed on screen
    display_array: list = []
    for index in phrase_array:
        # print(index)
        if index == " ":
            display_array.append("/ ")
        else:
            display_array.append("_ ")

    # create text to display from the array created above
    display_text: str = ''.join(display_array)
    start_text += f"The Word/Phrase is:\t {display_text} (Type *quit at any time to quit playing)"
    print(start_text)
    # End initialisation phase

    # Guess phase below
    is_winner = False
    letters_used = ""

    while num_guesses != 0 and not is_winner:
        # good_guess: 0 = null, 1 = true, 2 = false
        good_guess: int = 0
        print(f"\nGuesses remaining: {str(num_guesses)} \tLetters Attempted: {sort_letters(letters_used, ' ')}")
        current_guess: str = input("Enter your guess: ").upper()

        # check to see what type of guess player is making (full phrase, single letter or null)
        # full phrase guess
        if len(current_guess) > 1:
            # player wishes to quit
            if current_guess == "*QUIT":
                break
            # does full phrase guess match the game phrase?
            elif current_guess == game_phrase.upper():
                # player has guessed the phrase correctly and wins game immediately
                good_guess = 1
                is_winner = True
            else:
                good_guess = 2
        # null/space guess - player has pressed return by accident or has entered a space character
        elif len(current_guess) == 0 or current_guess == " ":
            good_guess = 0
        # letter guess
        else:
            # check that the guess is a valid character
            if check_char(current_guess) is not True:
                # character is a number (123...) or special char ("£%...")
                good_guess = 0
            # check to see if the player has already made a particular guess
            # either the player hasnt made a guess yet (letters used = 0) or
            # the player has made a guess that hasnt already been used
            elif len(letters_used) == 0 or letters_used.find(current_guess) == -1:
                # this is a brand new guess, add current guess to letters used string
                # letters_used = letters_used + current_guess
                letters_used += current_guess
                # do we have a match? start by assuming we dont (good guess is false)
                good_guess = 2
                for index, item in enumerate(phrase_array):
                    if str(item) == current_guess:
                        # we have a match
                        guessed_array.remove(item)
                        display_array[index] = item + " "
                        # we have at least 1 match so good guess
                        good_guess = 1
                # print(len(guessed_array))
                # print(phrase_array)
            else:
                good_guess = 0
                print(f"You have already tried the guess '{current_guess}' before, try again!")
        print(''.join(display_array).upper())

        if len(guessed_array) == 0:
            # all the letters in the phrase have been successfully guessed
            # player is a winner so set is_winner to True
            is_winner = True
            # player has already tried this guess before!

        if good_guess == 2:
            print("Incorrect guess, try again")
            num_guesses -= 1

    return is_winner


def check_word(phrase):
    """
        :rtype: bool
        :param phrase: string (non-numeric, non-zero length)
        :return: True if 0 length or contains numeric digits (0-9) else return False
    """

    if len(phrase) == 0:
        return True
    return any(i.isdigit() for i in phrase)


def check_char(character):
    if character.isalpha():
        return True
    else:
        return False


def word_count(phrase):
    # how many words in the phrase
    count = 1
    for letter in phrase:
        if letter == " ":
            count += 1
    return count


def sort_letters(letters, separator=None):
    """
    rtype: str
    :param letters: any string
    :param separator: character to separate sorted characters (e.g ' '). default is none
    :return: sorted string (with separator characters if supplied)
    """
    if separator is None:
        separator = ''
    return separator.join(sorted(letters))


def intro(version):
    welcome_text: str = f'''
    *** Welcome to the Hangman Game! ***
    *** Version {version} by James Davies ***
          _____
           |    |
           |   \\@/
           |    |
           |   / \\
          ---

    '''
    print(welcome_text)


intro(1.3)
default_guesses = 10
while True:
    guesses: str = input(f'How many guesses shall we have (default is {default_guesses})? \n')
    if check_word(guesses) is False:
        print("You must enter a number here\n")
    else:
        if len(guesses) == 0:
            guesses = str(default_guesses)
        while True:
            guess_word: str = input("Enter your guess word/phrase:\n")

            if check_word(guess_word) is True:
                print("You must enter a valid word/phrase without any numbers\n")
            else:
                break
        clue: str = input("Enter a clue if you wish: \n")
        print("\n")

        # print(hangman(int(guesses), guess_word, int(word_count(guess_word)), clue))
        if hangman(int(guesses), str(guess_word), int(word_count(guess_word)), str(clue)) is True:
            print("\nCongratulations you win!")

        else:
            print("\nUnlucky you lose!")
        break