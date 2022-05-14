from english_words import english_words_set
import random
import datetime
from colorama import Fore
english_words_set = list(english_words_set)
adb=0
a = True
word = ""
while(a):
  random.seed(datetime.datetime.utcnow().strftime("%f"))
  x = english_words_set[random.randint(0, 25487)]
  if len(x) == 5:
    word = x
    a = False

while(True):
  if adb== 5:
    break
  adb+=1
  guess = input("Enter your guess for the 5 letter word: ")
  if len(guess) != 5:
    continue
  b=0
  c = ""
  for i in guess:
    if i == word[b]:
      c = Fore.GREEN + i + Fore.WHITE 
      guess = guess.replace(i, c)
      b += 1
    elif i in word and i != word[b]:
      d = Fore.YELLOW + i + Fore.WHITE
      guess = guess.replace(i, d)
      b += 1
    else:
      b+=1

  print(guess)
  if guess == word:
    print("You found the word!")

print("You didnt find the word")
print("The word is "+word)
