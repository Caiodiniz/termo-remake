from random import choice         #choice randomly a word in the list
from unidecode import unidecode   #Remove accents

def remove_accents_and_uppercase(word):
  word_without_accents = unidecode(word).lower()
  return word_without_accents




#List of five letter word as an example to testing
five_letter_words = [
  "áureo", "média", "outro", "mesmo", "sagaz", "âmago", "negro", "termo", "êxito", "mexer",
  "ética", "plena", "mútua", "tênue", "fazer", "assim", "vigor", "sutil", "aquém", "porém",
  "seção", "fosse", "sanar", "poder", "audaz", "ideia", "cerne", "inato", "moral", "sobre",
  "desde", "muito", "justo", "honra", "quiçá", "torpe", "sonho", "razão", "etnia", "fútil",
  "ícone", "anexo", "amigo", "égide", "tange", "lapso", "haver", "expor", "dengo", "mútuo",
  "tempo", "nobre", "senso", "afeto", "algoz", "dança", "ameba"
]

#random_word = choice(five_letter_words)
random_word = five_letter_words[0] #áureo

user_word = input("Enter a 5-letter word: ")

#Ensure the typed word is in the list, with accents removed and in lowercase.
while remove_accents_and_uppercase(user_word) not in [remove_accents_and_uppercase(word) for word in five_letter_words]:
  user_word = input("Please, Enter a valid 5-letter word: ")

user_word_normalized = remove_accents_and_uppercase(user_word)
random_word_normalized = remove_accents_and_uppercase(random_word)

#for letter in user_word_normalized:

if(user_word_normalized == random_word_normalized):
  print("Words Matched!")