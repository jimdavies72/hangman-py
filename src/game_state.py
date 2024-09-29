from functions import phrase_display, remove_punctuation

def set_game_state(rules: dict) -> dict:

  game_state = {}
  
  game_state["letters_used"] = ""
  game_state["display_list"] = phrase_display(list(rules["guess_phrase"]))
  game_state["remaining_letters_list"] = rules["guess_phrase"].replace(" ", "")
  game_state["remaining_guesses"] = rules["guesses"]
  
  return game_state