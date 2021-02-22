import sys
import random
file = open("wof_words.txt", "r")
words_from_list = file.read().upper().split()
difficulty = input(" This is Wheel of Fortune! Select how you'd like to proceed. Easy, Normal, or Hard")
easy_words = [word.upper() for word in words_from_list if len(word) >= 4 and len(word) <= 6]
normal_words = [word.upper() for word in words_from_list if len(word) >=6 and len(word) <= 8]
hard_words = [word.upper() for word in words_from_list if len(word) >= 8]
stopguessing = 8

def random_word (selected_list):
    word = (random.choice (selected_list))
    return word.upper()

# Grouping words and level of difficulty for player to choose from.
difficulty = input(" How are you feeling? Choose your level of difficulty: Easy, Normal, or Hard ").upper()
if difficulty == "Easy": 
    random_word = random_word(easy_words).strip()
elif difficulty == "Normal":
    random_word = random_word(normal_words).strip()
elif difficulty == "Hard":
    random_word = random_word(hard_words).strip()

# # Game operation
print(random_word)

# player_guess = input('Give it a shot')
# if player_guess in selected_list: