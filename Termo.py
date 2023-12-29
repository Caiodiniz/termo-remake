from random import choice         #choice randomly a word in the list
from unidecode import unidecode   #Remove accents

def remove_accents_and_uppercase(word):
  word_without_accents = unidecode(word).lower()
  return word_without_accents

def create_list_game_word_letter_occurrences(word):
  letter_list = []

  for i in range(len(word)):
    letter_found = False

    for item in letter_list:
      if item[0] == word[i]:
        item[1] += 1
        letter_found = True
        break

    if not letter_found:
      auxiliary = [word[i], 1]
      letter_list.append(auxiliary)

  return letter_list

def count_occurrences(list_occurrences, letter):
  for item in list_occurrences:
    if item[0] == letter:
      return item[1]

def print_colored_letter(letter, color):
  colors = {
    'green': '\033[92m',
    'yellow': '\033[93m',
    'gray': '\033[90m',
    'reset': '\033[0m'
  }
  color_code = colors.get(color)
  print(f"{color_code}{letter}{colors['reset']}", end = '')


def print_word(status_list):
  status = {
    'match': 'green',
    'near': 'yellow',
    'clash': 'gray'
  }
  for item in status_list:
    print_colored_letter(item[0], status.get(item[1]))
  print()


# List of five letter word as an example to testing
five_letter_words = [
  "arara", "média", "outro", "mesmo", "sagaz", "âmago", "negro", "termo", "êxito", "mexer",
  "ética", "plena", "mútua", "tênue", "fazer", "assim", "vigor", "sutil", "aquém", "porém",
  "seção", "fosse", "sanar", "poder", "audaz", "ideia", "cerne", "inato", "moral", "sobre",
  "desde", "muito", "justo", "honra", "quiçá", "torpe", "sonho", "razão", "etnia", "fútil",
  "ícone", "anexo", "amigo", "égide", "tange", "lapso", "haver", "expor", "dengo", "mútuo",
  "tempo", "nobre", "senso", "afeto", "algoz", "dança", "ameba", "áureo", "amara", "carta"
]
#game_word = choice(five_letter_words)
game_word = five_letter_words[0]

matched = False
for attempt in range(8):

  user_word = input("Enter a 5-letter word: ")

  # Ensure the typed word is in the list, with accents removed and in lowercase.
  while remove_accents_and_uppercase(user_word) not in [remove_accents_and_uppercase(word) for word in five_letter_words]:
    user_word = input("Please, Enter a valid 5-letter word: ")

  # Assign normalized names to the words
  user_word_normalized = remove_accents_and_uppercase(user_word)
  game_word_normalized = remove_accents_and_uppercase(game_word)

  #Create a list to store the letters of game_word_normalized and their occurrences
  game_word_letter_occurrences = create_list_game_word_letter_occurrences(game_word_normalized)

  #Create a list to store the letters of user_word_normalized, initializing each one to 0
  user_word_letter_occurrences = []
  for letter in user_word_normalized:
      if [letter, 0] not in user_word_letter_occurrences:
          user_word_letter_occurrences.append([letter, 0])

  #Create a list where shows the status of each word compared to the random word
  letter_status = [list(char) for char in user_word_normalized]

  # Set "match" status to the letters in corresponding positions and add the ocorrence of this letter to when user_word_count_letter_occurrences matched
  for i in range(5):
    if(user_word_normalized[i] == game_word_normalized[i]):
      letter_status[i].append("match")
      for item in user_word_letter_occurrences:
        if item[0] == game_word_normalized[i]:
          item[1] += 1




  # Set "near" status to the letters in nearing positions.
  for i in range(5):
    k = 0
    while ((k < 5) and (user_word_normalized[i] != game_word_normalized[i])):
      # Ensure the letters match when not in the same position, as this case has already been treated before.
      if(user_word_normalized[i] == game_word_normalized[k]):
        if (count_occurrences(user_word_letter_occurrences, user_word_normalized[i]) <
            count_occurrences(game_word_letter_occurrences, user_word_normalized[i])):
          letter_status[i].append("near")
          break
      k += 1
    for item in user_word_letter_occurrences:
      if item[0] == user_word_normalized[i]:
        item[1] += 1

  # Set "clash" status to the letters not in word
  for item in letter_status:
    if len(item) == 1:
      item.append("clash")


  print_word(letter_status)

  if(user_word_normalized == game_word_normalized):
    matched = True
    break

if matched:
  print("Words Matched!")
else:
  print("Game Over!")