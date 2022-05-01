import random

# How to play the game
print("Wordle \nGuess the 5-letter Word, you have 6 guesses \n If the word you guessed has a letter in the right spot in the right word, it will be 'G' \n If the word you guessed has a letter of the right word, but in the wrong spot, it will be 'Y' \n If the letter isn't in the correct word, it will be '-' \n\n\n")

# Create a function to get the users guess 
def retrieveGuess():
    guess = input("Guess a 5-letter word: ")
    if len(guess) > 5:
        print("\nPlease enter a 5-letter word")
        guess = retrieveGuess()
    return guess

# Defining the algorithm to check the user's guess
def checkGuess(CorrectAnswer, userGuess):
  position = 0
  clue = ""

  # Letting the user know if the position of the letter guessed is correct
  for letter in userGuess:
    if letter == CorrectAnswer[position]:
      clue += "G"
    elif letter in CorrectAnswer:
      clue += "Y"
    else:
      clue += "-"
    position += 1
  print(clue)
  return clue == "GGGGG"  # True if correct, False otherwise


# Loading all of the words from "words.txt" and adding them to a list
## The "words.txt" is from The Free Dictionary -- https://www.thefreedictionary.com/5-letter-words.htm
word_list = []
word_file = open("words.txt")
for word in word_file:
  word_list.append(word.strip())


# Picking a random word
answer = random.choice(word_list)

num_of_guesses = 0
correctly_guessed = False

while num_of_guesses < 6 and not correctly_guessed:
  # Getting the guess from user
  guess = retrieveGuess()
  print("You guessed", guess)
  num_of_guesses += 1  # adding the number of total guesses
  # Process the guess
  correctly_guessed = checkGuess(answer, guess)  # calling the function

  # Letting the user know how many guesses are left
  guesses_left = 6 - num_of_guesses
  print("You have", guesses_left, "guesses left!\n\n")


# End of game messages

if correctly_guessed:
  print("Congratulations! You guessed the correct word in", num_of_guesses, "times!")
else:
  print("You are out of guesses, the correct word is", answer)
