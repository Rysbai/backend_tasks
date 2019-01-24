# TASK
# You are given a positive integer N. 
# Print a numerical triangle of height N - 1 like the one below:

# 1
# 22
# 333
# 4444
# 55555

# Can you do it using only arithmetic operations, 
# a single for loop and print statement?

# Use no more than two lines. The first line (the for statement) is 
# already written for you. You have to complete the print statement.


import functools
for i in range(1,int(input())): 
    print(functools.reduce(lambda a, b: a + b, 
                            list(i*(10**power) for power in range(i-1, -1, -1))))

# Я не смог делать с одной строкой