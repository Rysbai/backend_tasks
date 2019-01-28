
# TASK
# You are given n words. Some words may repeat. For each word, output 
# its number of occurrences. The output order should correspond with the 
# input order of appearance of the word. See the sample input/output for clarification.

# Note: Each input line ends with a "\n" character.

# Link to problem:
# https://www.hackerrank.com/challenges/word-order/problem

distinct_words = {}

for i in range(int(input())):
    word = input()
    if word in distinct_words:
        distinct_words[word] += 1
    else:
        distinct_words[word] = 1

print(len(distinct_words))

print(*list(value for value in distinct_words.values()))