import random

def words():
  """
  This function reads a random word from the "word.txt" file.
  """
  with open("words.txt", "r") as f:
    
        content = f.readlines()
    # Remove trailing newline characters from words
        word_list = [word.strip() for word in content]
        answer = random.choice(word_list)
        return answer.upper()


def play():
  """
  This function handles the game logic for Hangman.
  """
  answer = words()  # Get the random word (already uppercase)
  word_length = len(answer)
  print(answer)

  # Create a hidden word representation with underscores
  hidden_word = "_" * word_length

  guessed = False
  letters_used = []
  correct_used=[]
  tries = word_length  

  print("Let's play Hangman!")
  print(hidden_word)

  stages = [  # List of hangman stages (order matters here)
        """
        --------
        |      |
        |      O
        |     /|\
        |     / \
        |
        |
        -------
    """
    """
        --------
        |      |
        |      O
        |     /|\
        |     /
        |
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |     /|\
        |
        |
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |     /|
        |
        |
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |      |
        |
        |
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |     
        |
        |
        -------
    """
  ]

  print(stages[tries-1])
  print()

  while not guessed and tries > 0:
    guess = input("Guess a letter: ").upper()

    # Check for valid guess (single letter)
    if len(guess) == 1 and guess.isalpha():
      if guess in answer:
        # Update hidden word with correct guess
        new_hidden_word = ""
        for i in range(word_length):
          if answer[i] == guess:
            new_hidden_word += guess
          else:
            new_hidden_word += hidden_word[i]
        hidden_word = new_hidden_word

        print(hidden_word)
        correct_used.append(guess)  # Removed unused variable

      elif guess not in answer:
        tries -= 1
        letters_used.append(guess)
        print("Wrong guess. You have", tries, "tries left.")

      

    else:
       print("Invalid guess. Please enter a single letter.")

    print(stages[tries-1])  # Update hangman stage based on tries remaining


  # Game over message
  if guessed:
    print("Congratulations! You guessed the word:", answer)
  else:
    print("You ran out of tries. The word was:", answer)

words()  # Call the function to start the game
play()

