
# Task
# Students of District College have a subscription to English and French newspapers. 
# Some students have subscribed to only the English newspaper, some have subscribed to only the 
# French newspaper, and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English n
# ewspaper, and one set has subscribed to the French newspaper. Your task is to find the total 
# number of students who have subscribed to only English newspapers.

# Input Format

# The first line contains the number of students who have subscribed to the English newspaper. 
# The second line contains the space separated list of student roll numbers who have subscribed 
# to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper. 
# The fourth line contains the space separated list of student roll numbers who have subscribed to 
# the French newspaper.


n = int(input())
n_roll_numbers = set(input().split(" "))
b = int(input())
b_roll_numbers = set(input().split(" "))

print(len(n_roll_numbers - b_roll_numbers))