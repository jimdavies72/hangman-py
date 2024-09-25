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
  cls(1)
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

def cls(wait: int = 0) -> None:
  if type(wait) != int:
    time.sleep(0)
  else:  
    time.sleep(wait)
  os.system('cls')

def contains_numbers(text: str) -> bool:
  return any(char.isdigit() for char in text)
  