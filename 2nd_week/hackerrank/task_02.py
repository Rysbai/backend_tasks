
# Task 
# Given an integer, N, perform the following conditional actions:

# If N is odd, print Weird
# If N is even and in the inclusive range of 2 to 5, print Not Weird
# If N is even and in the inclusive range of 6 to 20, print Weird
# If N is even and greater than 20, print Not Weird


N = int(input())

if N % 2 != 0:
    print("Weird")
elif (N % 2 == 0):
    if (N >= 2) and (N <= 5):
        print("Not Weird")
    elif (N >= 6) and (N <= 20):
        print("Weird")
    elif (N > 20):
        print("Not Weird")
