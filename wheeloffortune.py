import sys
import random
file = open("wof_words.txt", "r")
words_from_list = file.read().upper().split()
difficulty = input(" This is Wheel of Fortune! Select how you'd like to proceed. Easy, Normal, or Hard ").upper()
easy_words = [word.upper() for word in words_from_list if len(word) >= 4 and len(word) <= 6]
normal_words = [word.upper() for word in words_from_list if len(word) >=6 and len(word) <= 8]
hard_words = [word.upper() for word in words_from_list if len(word) >= 8]
stopguessing = 8

def get_random_word (selected_list):
    word = (random.choice (selected_list))
    return word.upper()

# Grouping words and level of difficulty for player to choose from.
random_word = ''
if difficulty == "EASY": 
    random_word = get_random_word(easy_words).upper().strip()
elif difficulty == "NORMAL":
    random_word = get_random_word(normal_words).upper().strip()
elif difficulty == "HARD":
    random_word = get_random_word(hard_words).upper().strip()

# # Game operation
display_letter_blocks = ['_' for letter in range(len(random_word))]
print(' '.join(display_letter_blocks))
player_guess = input('Give it a shot!! ')
guessed_words = []
# display_letter_blocks = (len(random_word) * "_ ")
if player_guess in random_word:
    for index in range(len(random_word)):
        if player_guess == random_word[index]:
            display_letter_blocks[index]=player_guess
            print("You got it!")
            guessed_words.append(player_guess)

    
else:
    stopguessing -= 1
    print(f"Sorry! Try again. You have {stopguessing} tries left.")




# # for letter in random_word:
# #     if letter in random_word:
# #         print(letter)
# # if player_guess in selected_list: