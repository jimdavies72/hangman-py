# All game code related to parameters and rules

from  functions import *

DEFAULT_GUESSES = 10

def get_guess_limit() -> int:
  good_response = False
  
  while not good_response:
    whitespace()
    
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
    whitespace()
    
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
    whitespace()
    
    clue = question("Enter a clue if you wish:")
    
    if len(clue) == 0:
      response = question("Are you sure you don't want to add a clue? (y/n)")
      
      if response == "y".lower() or response == "":
        clue = "No clue provided"
        good_response = True 
        
    else:
      good_response = True
  
  return clue

def include_numbers() -> bool:
  cls(1)
  whitespace()
  response = question("Include numbers in the word/phrase? (y/n)")
  
  if response == "y".lower():
    return True

  return False
    
def display_rules(rules: dict) -> None:
  cls()
  whitespace()
  
  if rules["include_numbers"] == True:
    include_numbers = " may be used in this game"
  else:
    include_numbers = " are not used in this game"
  text = f"{rules["phrase_contrast"]}: {rules["word_count"]} {rules["word_plural"]}\nYou have: {rules["guesses"]} {rules["guess_contrast"]}\nThe clue is: {rules['clue']}\nNumbers{include_numbers}"
  
  print(box_text(text))
  whitespace(2)
  information("(Type *quit at any time to quit playing)")
  
  cls(4)

def set_rules() -> dict:
  # The rules are set at the beginning of the then dont change
  rules = {}

  rules["guesses"] = get_guess_limit()
  rules["include_numbers"] = include_numbers()
  rules["guess_phrase"] = get_guess_phrase(rules["include_numbers"])
  rules["word_count"] = len(rules["guess_phrase"].split(" "))
  rules["clue"] = get_clue()
  
  # set the game word contrasts
  if rules["word_count"] > 1:
    rules["phrase_contrast"] = "There are"
    rules["word_plural"] = "words"
  else:
    rules["phrase_contrast"] = "There is"
    rules["word_plural"] = "word"
  
  if rules["guesses"] > 1:
    rules["guess_contrast"] = "guesses"
  else:
    rules["guess_contrast"] = "guess"
  
  display_rules(rules)
  
  return rules
