
# TASK
# You are given a positive integer N. 
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:
# 1
# 121
# 12321
# 1234321
# 123454321

# Link to problem:
# https://www.hackerrank.com/challenges/triangle-quest-2/problem


for i in range(1,int(input())+1): 
    print(sum(10**power for power in range(i-1, -1, -1))**2)
