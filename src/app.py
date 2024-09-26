from game_set_up import *
  
def phrase_display(phrase: str) -> list:
  # how the phrase will be displayed on screen
  display_phrase = []
  for letter in phrase:
    if letter == " ":
      display_phrase.append("/ ")
    else:
      display_phrase.append("_ ")
  
  return display_phrase

def check_guess(phrase: str, include_numbers: bool, guess: str, letters_used: str) -> int:
  if is_number_state_good(include_numbers, contains_numbers(guess)):
    if len(guess) > 1:
      # phrase guess
      if guess == phrase:
        return GT.WIN
      else:
        return GT.BAD
    elif len(guess) == 0:
      # accidental return or "" after invalid chars removed. allow as a non-guess
      return GT.NULL
    elif guess in letters_used:
      return GT.NULL
    elif guess not in phrase:
      return GT.BAD
    else:
      # was a good guess
      return GT.GOOD 
  else:
    return GT.NULL

def guess_phase(game_params: dict) -> bool:
  is_winner = False
  letters_used = ""
  
  while game_params["guesses"] > 0 and not is_winner:
    command(f"Guesses remaining: {game_params['guesses']}")
    
    if len(letters_used) > 0:
      command(f"Letters used: {letters_used}")
      
    # We dont want to have a space or punctiation as a guess as these are not allowed in the game
    guess = remove_punctuation(question("Enter your guess:").upper(), True)
    
    if guess == "*QUIT":
      break
    else:
      
        match check_guess(game_params["guess_phrase"], game_params["include_numbers"], guess, letters_used):
        
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
  
  print(box_text(text))
    
main()