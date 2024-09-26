# All game code related to parameters and rules

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
    guess_phrase = question(f"Enter the word/phrase to guess{inc_nums_text}:").upper()
    
    if len(guess_phrase) == 0:
      warning("You must enter a word/phrase")
      cls(1)
    elif not is_number_state_good(include_numbers, contains_numbers(guess_phrase.replace(" ", ""))):
      # numbers not allowed but user entered a number
      warning("You must enter a word/phrase without any numbers")
      cls(2)
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
  cls(1)
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
