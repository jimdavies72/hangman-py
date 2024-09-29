from game_rules import *
from game_state import set_game_state

def display_game_state(game_state: dict) -> None:
  whitespace()
  
  command(f"The word/phrase is: {''.join(game_state['display_list'])}")
  whitespace()
  
  command(f"Guesses remaining: {game_state['remaining_guesses']}")
  whitespace()
  
  if len(game_state['letters_used']) > 0:
    command(f"Letters used: {game_state['letters_used']}")
    whitespace()

def check_guess(rules: dict, guess: str, letters_used: str) -> int:
  if is_number_state_good(include_numbers, contains_numbers(guess)):
    if len(guess) > 1:
      # phrase guess  
      if guess == rules["guess_phrase"]:
        return GT.WIN
      else:
        return GT.BAD
    elif len(guess) == 0 or guess == " ":
      # accidental return or "" after invalid chars removed. allow as a non-guess
      return GT.NULL
    elif guess in letters_used:
      return GT.NULL
    elif guess not in rules["guess_phrase"]:
      return GT.BAD
    else:
      # was a good guess
      return GT.GOOD 
  else:
    return GT.NULL

def hangman(rules: dict) -> list:
  try:
    is_end_game = False
    result = ""
    
    game_state = set_game_state(rules)
  
    while game_state["remaining_guesses"] > 0 and not is_end_game:
      display_game_state(game_state)
      whitespace()
      
      guess = question("Enter your guess:").upper()
      if guess == "*QUIT":
        result = "quit"
        break
      guess = remove_punctuation(guess.strip(), False)
        
      match check_guess(rules, guess, game_state["letters_used"]):
        case GT.GOOD:
          # remove all occurances of the letter in the phrase
          game_state["letters_used"] += guess
          game_state["remaining_letters_list"] = game_state["remaining_letters_list"].replace(guess.upper(), "")
  
          if len(game_state["remaining_letters_list"]) == 0:
            result = "win"
            is_end_game = True
          else:
            for i, letter in enumerate(rules["guess_phrase"]):
              if letter == guess:
                game_state["display_list"][i] = guess + " "
        case GT.BAD:
          whitespace()
          warning("Incorrect guess")
          if len(guess) == 1:
            game_state["letters_used"] +=  guess
            
          game_state["remaining_guesses"] -= 1 
          if game_state["remaining_guesses"] == 0:
            result = "lose"
        case GT.WIN:
          is_end_game = True
          result = "win"
        case GT.NULL:
          pass
      
      cls(1)
      
    return [result, rules["guess_phrase"]]
  
  except Exception as e:
    print(ex(e, inspect.stack()[0][3]))

def main():
  cls()
  intro(2.0)
  cls(2)
  
  result: list = hangman(set_rules())
  
  whitespace()
  
  if result[0] == "win":
    text = f"Congratulations you win!\nThe word/phrase was: {result[1]}"
  elif result[0] == "lose":
    text = f"Unlucky you lose!\nThe word/phrase was: {result[1]}"
  else:
    text = f"Thanks for playing, sorry to see you go\nThe word/phrase was: {result[1]}"
    
  print(box_text(text))
  whitespace(2)
  
main()