import inspect, math
import string as s

# foreground colours
sgr = '\033[1;3'
RED = sgr + '1m'
GREEN = sgr + '2m'
YELLOW = sgr + '3m'
BLUE = sgr + '4m'
MAGENTA = sgr + '5m'
CYAN = sgr + '6m'
NC = '\033[0m'

stack = inspect.stack()[0][3]

def ex(message: str, stack: str) -> str:
  # func: format exception message
  # params: message to print
  #         result of inspect.stack() @ time
  
  return f"{RED}Exception: '{message}' occured in: {stack}(){NC}"

def list_longest(input_list: list) -> int:
  # func:   returns the length of the longest item in the input list
  # params: list of items  
  try:
    if type(input_list) == list:
      return len(max(input_list, key=len))
    else:
      raise Exception("Incorrect arguement Type")
  
  except Exception as e:
    print(ex(e, stack))

def pad_text(text: str, max_length: int, pad_pos: str) -> str:
  # func:   creates a padded fixed length string
  # params: the text you wish to pad. 
  #         max_length to pad to (e.g *Hello     *)
  #         pad to left, right or left/right
  
  try: 
    if len(text) >= max_length:
      raise Exception("Text exceeds max length")
    else:
      pad = (max_length - len(text)) * " "
      
      match pad_pos:
        case "left":
          text = pad + text
        case "right":
          text = text + pad
        case _:
          half_pad = math.floor(len(pad) / 2) * " "
          
          if len(text) % 2 == 0:
            text = half_pad + text + half_pad
          else:
            text = " " + half_pad + text + half_pad

    return text

  except Exception as e:
    print(ex(e, stack))

def box_text(text):
  # func:   creates a red border of * around lines of text
  # params: formatted text --> ""hello\nthis is the\nend of the world"" 

  try:
    text_list = text.splitlines()
    max_length = list_longest(text_list) + 4
    
    border = [f"{RED}{'*' * (max_length + 4)}"]

    for line in text_list:
      border.append(f"*{GREEN}{pad_text(line, max_length + 2, "centre")}{RED}*")
    
    border.append(f"{'*' * (max_length + 4)}{NC}")
    
    return "\n".join(border)
  
  except Exception as e:
    print(ex(e, stack))

def remove_punctuation(text: str, include_spaces: bool = False) -> str:
  # func:   removes punctuation from the text
  # params: text to remove punctuation from
  
  try:
    # replace hyphens with " " first
    text = text.replace("-", " ")

    # remove all other punctuation
    for char in text:
      if char in s.punctuation:
        text = text.replace(char, "")

    if include_spaces:
      # remove all spaces
      text = text.replace(" ", "")

    return text

  except Exception as e:
    print(ex(e, stack))
