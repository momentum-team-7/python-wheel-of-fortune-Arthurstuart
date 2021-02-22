# Mystery Word
Github link - https://github.com/momentum-team-7/python-wheel-of-fortune-Arthurstuart.git
## Description

Implement the game of Mystery Word.

## Objectives

After completing this assignment, you should be able to:

- Create an interactive program.
- Read from a file.
- Choose a random value.
- Keep track of state.

## Details

## Normal Mode

You will implement the game Mystery Word. In your game, you will be playing
against the computer.
- [ ]  player_1 
- [ ]  cpu 

The computer must select a word at random from the list of words in the file
`words.txt` from this repository.
<!-- - Read the file and store the items in a list.
- Select a word from the word list. -->

The game must be interactive; the flow of the game should go as follows:

<!-- 1. Let the user choose a level of difficulty at the beginning of the program.
   Easy mode only has words of 4-6 characters; normal mode only has words of 6-8
   characters; hard mode only has words of 8+ characters.
   - List of easy, medium, and hard words. This is based on the # of characters.
   - Create levels of difficulty for the user to choose from (choose from differnt type - list, dictionary) -->

2. At the start of the game, let the user know how many letters the computer's
   word contains.
   - Count the number of letters in the word
   - Display one blank for each word (look up the join method) 

3. Ask the user to supply one guess (i.e. letter) per round. This letter can be
   upper or lower case and it should not matter. If a user enters more than one
   letter, tell them the input is invalid and let them try again.
   - Ask the user to guess a letter 
   - Store letter guessed
   - Create an error message for more than one letter at once.

4. Let the user know if their guess appears in the computer's word.
- Create process to determine whether a guess is correct. 
- Store the guesses (which one of the letters have correctly been guessed? Which ones have been incorrectly guessed?)
- Alert player that they've guessed a letter correctly (print they've gotten it right)

5. Display the partially guessed word, as well as letters that have not been
   guessed. For example, if the word is BOMBARD and the letters guessed are a, b,
   and d, the screen should display:
- Display right and wrong guesses (see below)

```
B _ _ B A _ D
```
---------------------------------

A user is allowed 8 guesses. Remind the user of how many guesses they have left
after each round.
- Set up a maxiumum of 8 guesses 
- End the game once they've reached eight incorrect guesses.

_A user loses a guess only when they guess incorrectly._ If they guess a letter
that is in the computer's word, they do not lose a guess.
- If the answer is right, a new display featuring correctly guessed letters to the word at play. If they guess wrong, add towards the tally of incorrect responses. If that gets to eight incorrect guesses the game ends.

If the user guesses the same letter twice, do not take away a guess. Instead,
print a message letting them know they've already guessed that letter and ask
them to try again.
- No changes to the number of incorrect guesses. 

The game should end when the user constructs the full word or runs out of
guesses. If the player runs out of guesses, reveal the word to the user when
the game ends.
- The player wins when they guess the whole word and the game is over.

When a game ends, ask the user if they want to play again. The game begins
again if they reply positively.

## Hard Mode

Implement the [evil version of this game](http://nifty.stanford.edu/2011/schwarz-evil-hangman/).
Put it in a new Python program called "demon_words.py".

## Credit

This lab is based off a similar exercise in MIT's 6.00.1x course.
