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
  
def get_guess_phrase() -> str:
  good_response = False
  
  while not good_response:
    cls(1)
    guess_phrase = question("Enter your guess word/phrase:").upper()
    
    if len(guess_phrase) == 0:
      warning("You must enter a word/phrase")
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
      response = question("Are you sure you don't want a clue?")
      
      if response == "y".lower():
        clue = "No clue"
        good_response = True 
        
      cls(1)
    else:
      good_response = True
  
  return clue

def display_rules(game_params: dict) -> None:
  cls()
  text = f"{game_params["phrase_contrast"]}: {game_params["word_count"]} {game_params["word_plural"]}\nYou have: {game_params["guesses"]} {game_params["guess_contrast"]}\nThe clue is: {game_params['clue']}"
  
  print(box_text(text))
  

def set_game_params() -> dict:
  game_params = {}

  game_params["guesses"] = get_guess_limit()
  game_params["guess_phrase"] = get_guess_phrase()
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

def hangman(game_params: dict) -> bool:
  try:
    phrase_list = game_params["guess_phrase"].split()
    guessed_list = game_params["guess_phrase"].replace(" ", "")
    display_list = phrase_display(game_params["guess_phrase"])
    
    cls(2)
    command(f"The word/phrase is: {"".join(display_list)} (Type *quit at any time to quit playing)")
    
    return True # test return for now
  
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