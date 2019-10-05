import random

HANGMAN = (
"""
----
|
|
|
|
|
|
|
|
|
----------
""",
"""
----
|   |
|
|
|
|
|
|
|
|
----------
""",
"""
----
|   |
|   |
|   O
|   |
|  -+-
|
|
|
|
|
----------
""",
"""
----
|
|
|
O
|
/-+-
|
|
|
|
|
----------
""",
"""
----
|
|
|
O
|
/-+-/
|
|
|
|
|
----------
""",
"""
----
|
|
|
O
|
/-+/
|
|
|
|
|
|
----------
""",
"""
----
|
|
|
O
|
/-+/
|
|
|
|
|
|
|
|
|
----------
""",
"""
----
|
|
|
O
|
/-+/
|
|
|
|
|
| |
|
| |
|
----------
""")
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "PUCK", "TAFFETA")
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print"Welcome to Hangman. Good Luck!"
while(wrong < MAX_WRONG) and (so_far != word):
    print HANGMAN[wrong]
    print"\nYou've guessed the following letters: ", used
    print"\nSo far the word is ", so_far
    guess = raw_input("\n\nEnter your guess: ")
    guess = guess.upper()
    while (guess in used):
        print "You've already guessed the letter:", guess
        guess = raw_input("Enter your guess: ")
        guess = guess.upper()
    used.append(guess)
    if (guess in word):
        print "\nYes!", guess, "is in the word!"
        # create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print"\nSorry not in the word"
        wrong += 1
if(wrong == MAX_WRONG):
    print HANGMAN[wrong]
    print "You've been hanged!"
else:
    print"You guessed the word!"
print"The word was ", word
raw_input("\n\nPress enter to exit!")
