# TASK
# You are given a positive integer N. 
# Print a numerical triangle of height N - 1 like the one below:

# 1
# 22
# 333
# 4444
# 55555


for i in range(1,int(input())): 
    print(list(i*(10**power) for power in range(i-1, 0, -1)))


# My output: 

# []
# [20]
# [300, 30]
# [4000, 400, 40]

# Пока что так