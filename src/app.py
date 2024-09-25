from  functions import *

DEFAULT_GUESSES = 10

def get_guess_limit() -> int:
  good_response = False
  
  while not good_response:
    guess_limit = question(f"How many guesses shall we have (default is {DEFAULT_GUESSES})?")
    
    if len(guess_limit) == 0:
      guess_limit = DEFAULT_GUESSES
      good_response = True
    elif guess_limit.isalpha():
      warning("You must enter numbers (0-9)")
      cls(1)
    elif int(guess_limit) < 1 or int(guess_limit) > 26:
      warning("Guess limit is outside viable limits (1 - 26)")
      cls(1)
    else:
      good_response = True
      
  return int(guess_limit)
  
def get_guess_phrase(include_numbers: bool) -> str:
  good_response = False
  
  inc_nums_text = ""
  if include_numbers:
    inc_nums_text = " (numbers are allowed)"
  else:
    inc_nums_text = " (numbers are not allowed)"
  
  while not good_response:
    cls(1)
    guess_phrase = question(f"Enter your guess word/phrase:{inc_nums_text}").upper()
    
    if len(guess_phrase) == 0:
      warning("You must enter a word/phrase")
      cls(1)
    elif include_numbers == False and guess_phrase.isalpha() == False:
      # numbers not allowed but user entered a number
      warning("You must enter a word/phrase without any numbers")
      cls(1)
    else:
      # strip out any punctuation
      guess_phrase = remove_punctuation(guess_phrase)
      good_response = True
  
  return guess_phrase 

def get_clue() -> str:
  good_response = False
  
  while not good_response:
    cls(1)
    clue = question("Enter a clue if you wish:")
    
    if len(clue) == 0:
      response = question("Are you sure you don't want to add a clue? (y/n)")
      
      if response == "y".lower() or response == "":
        clue = "No clue"
        good_response = True 
        
      cls(1)
    else:
      good_response = True
  
  return clue

def include_numbers() -> bool:
  response = question("Include numbers in the word/phrase? (y/n)")
  
  if response == "y".lower():
    return True

  return False
    
def display_rules(game_params: dict) -> None:
  if game_params["include_numbers"] == True:
    include_numbers = " may be used in this game"
  else:
    include_numbers = " are not used in this game"
  text = f"{game_params["phrase_contrast"]}: {game_params["word_count"]} {game_params["word_plural"]}\nYou have: {game_params["guesses"]} {game_params["guess_contrast"]}\nThe clue is: {game_params['clue']}\nNumbers{include_numbers}"
  
  cls(3)
  
  print(box_text(text))
  
def set_game_params() -> dict:
  game_params = {}

  game_params["guesses"] = get_guess_limit()
  game_params["include_numbers"] = include_numbers()
  game_params["guess_phrase"] = get_guess_phrase(game_params["include_numbers"])
  game_params["word_count"] = len(game_params["guess_phrase"].split(" "))
  game_params["clue"] = get_clue()
  
  if game_params["word_count"] > 1:
    game_params["phrase_contrast"] = "There are"
    game_params["word_plural"] = "words"
  else:
    game_params["phrase_contrast"] = "There is"
    game_params["word_plural"] = "word"
  
  if game_params["guesses"] > 1:
    game_params["guess_contrast"] = "guesses"
  else:
    game_params["guess_contrast"] = "guess"
  
  display_rules(game_params)
  
  return game_params

def phrase_display(phrase: str) -> list:
  # how the phrase will be displayed on screen
  display_phrase = []
  for letter in phrase:
    if letter == " ":
      display_phrase.append("/ ")
    else:
      display_phrase.append("_ ")
  
  return display_phrase

def check_guess(guess: str, phrase: str, include_numbers: bool, letters_used: str) -> int:
  if len(guess) > 1:
    # phrase guess
    if guess == phrase:
      return GT.WIN
    else:
      return GT.BAD
  elif len(guess) == 0 or guess == " ":
    # space submitted or accidental return. allow as a non-guess
    return GT.NULL
  elif not include_numbers and contains_numbers(guess):
    # if games doesnt allow numbers but user entered a number
    # as a guess. allow as a non-guess
    return GT.NULL
  elif guess in letters_used:
    return GT.NULL
  elif guess not in phrase:
    return GT.BAD
  else:
    # was a good guess
    return GT.GOOD 

def guess_phase(game_params: dict) -> bool:
  is_winner = False
  letters_used = ""
  
  while game_params["guesses"] > 0 and not is_winner:
    command(f"Guesses remaining: {game_params['guesses']}")
    if len(letters_used) > 0:
      command(f"Letters used: {letters_used}")
    guess = question("Enter your guess:").upper()
    
    if guess == "*QUIT":
      break
    else:
      match check_guess(guess, game_params["guess_phrase"], game_params["include_numbers"], letters_used):
      
        case GT.WIN:
          is_winner = True
        case GT.GOOD:
          letters_used = letters_used + guess
        case GT.BAD:
          game_params["guesses"] -= 1
          warning("Bad guess :'(")
          letters_used = letters_used + guess
        case GT.NULL:
          pass
    cls(2)
    
  return is_winner

def hangman(game_params: dict) -> bool:
  try:
    phrase_list = game_params["guess_phrase"].split()
    guessed_list = game_params["guess_phrase"].replace(" ", "")
    display_list = phrase_display(game_params["guess_phrase"])
    
    cls(2)
    command(f"The word/phrase is: {"".join(display_list)} (Type *quit at any time to quit playing)")
    
    return guess_phase(game_params)
  
  except Exception as e:
    print(ex(e, inspect.stack()[0][3]))

def main():
  intro(2.0)
  
  cls(2)
  if hangman(set_game_params()):
    text = "Congratulations you win!"
  else:
    text = "Unlucky you lose!"
  
  cls(1)
  print(box_text(text))
    
main()