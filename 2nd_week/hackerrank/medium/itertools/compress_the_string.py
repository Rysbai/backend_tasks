# TASK
# In this task, we would like for you to appreciate the usefulness of the groupby() function 
# of itertools . To read more about this function, Check this out .

# You are given a string S. Suppose a character 'c' 
# occurs consecutively X times in the string. Replace these consecutive occurrences of 
# the character 'c' with (X, c) in the string.


from itertools import groupby

string = input()
result = [(len(list(c)), int(k)) for k, c in groupby(string)]

print(*result)
