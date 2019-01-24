# TASK
# You are given a positive integer N. 
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:

# 1
# 121
# 12321
# 1234321
# 123454321

for i in range(1,int(input())+1): 
    print(sum(10**power for power in range(i-1, -1, -1))**2)

# 

# 10^0 = 1
# 10^1 + 1 = 11
# 10^2 + 10^1 + 1 = 111
# 10^3 + 10^2 + 10^1 + 1 = 1111
# 10^4 + 10^3 + 10^2 + 10^1 + 1 = 11111

# 1^2 = 1
# 11^2 = 121
# 111^2 = 12321
# 1111^2 = 1234321
# 11111^2 = 123454321