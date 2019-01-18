
# TASK
# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# https://www.hackerrank.com/challenges/the-minion-game/problem


import re

def minion_game(string):
    pattern = ['A', 'E', 'I', 'O', 'U']

    kevin_score = 0
    stuart_score = 0
    kevin_words = []
    stuart_words = []

    letter_index = 0
    for letter in string:
        if letter in pattern:
            if letter not in kevin_words:
                kevin_words.append(letter)
                
            ltr_index = 2
            for i in range(len(string) - letter_index):
                if ltr_index > len(string):
                    pass
                else: 
                    word = string[letter_index: letter_index+ltr_index]
                    if word not in kevin_words:
                        kevin_words.append(word)

                ltr_index += 1
        else:
            if letter not in stuart_words:
                stuart_words.append(letter)

            ltr_index = 2
            for i in range(len(string) - letter_index):
                if ltr_index > len(string):
                    pass
                else:
                    word = string[letter_index: letter_index+ltr_index]
                    if word not in stuart_words:
                        stuart_words.append(word)

                ltr_index += 1

        letter_index += 1

    for word in kevin_words:
        kevin_score += len(re.findall(word, string))

    for word in stuart_words:
        stuart_score += len(re.findall(word, string))


    if kevin_score > stuart_score:
        print("Kevin " + str(kevin_score))

    if stuart_score > kevin_score:
        print("Stuart " + str(stuart_score))


if __name__ == '__main__':
    s = input()
    minion_game(s)