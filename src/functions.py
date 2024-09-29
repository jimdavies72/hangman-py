from helper_functions import *
import os, time
from enum import Enum

# Guess result type
class GT(Enum):
  NULL = 0 # accidental or space
  GOOD = 1 # good guess
  BAD = 2 # bad guess
  WIN = 3 # winning guess or state

def intro(version: str) -> None:
  text = f"Welcome to the Hangman Game!\nVersion {version} by James Davies\n_____\n|    |\n|   \@/\n|    |\n|   / \\\n-------"
  
  print(box_text(text))

def question(text: str) -> str:
  if len(text) >= 1:
    return input(f"{BLUE}{text}{NC} ")

def warning(text: str) -> None:
  if len(text) >=1:
    print(f"{RED}{text}{NC}")

def command(text: str) -> None:
  if len(text) >= 1:
    print(f"{YELLOW}{text}{NC}")

def information(text: str) -> None:
  if len(text) >= 1:
    print(f"{GREEN}{text}{NC}")

def cls(wait: int = 0) -> None:
  if type(wait) != int:
    time.sleep(0)
  else:  
    time.sleep(wait)
  os.system('cls')

def is_number_state_good(numbers_allowed: bool, contains_numbers: bool ) -> bool:
  if numbers_allowed and contains_numbers:
    # numbers are allowed and value contains numbers
    return True
  elif numbers_allowed and contains_numbers == False:
    # numbers are allowed and value does not contain numbers
    return True
  elif numbers_allowed == False and contains_numbers:
    return False
  else:
    return True
  
def phrase_display(phrase: str) -> list:
  # how the phrase will be displayed on screen
  display_phrase = []
  for letter in phrase:
    if letter == " ":
      display_phrase.append("/ ")
    else:
      display_phrase.append("_ ")
  
  return display_phrase