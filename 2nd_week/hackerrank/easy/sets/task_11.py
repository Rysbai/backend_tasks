# TASK
# You are given a set A and N number of other sets. These N number of sets have to perform 
# some specific mutation operations on set A.

# Your task is to execute those operations and print the sum of elements from set A.

# Input Format

# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2*N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation 
# name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.


quantity = int(input())
set_a = set(input().split(" "))

N = int(input())

for i in range(1, N+1):
    operation_and_number = list(input().split(" "))
    set_n = set(input().split(" "))

    if operation_and_number[0] == "update":
        set_a.update(set_n)

    if operation_and_number[0] == "intersection_update":
        set_a.intersection_update(set_n)

    if operation_and_number[0] == "difference_update":
        set_a.difference_update(set_n)

    if operation_and_number[0] == "symmetric_difference_update":
        set_a.symmetric_difference_update(set_n)


sum_a = 0

for i in set_a:
    sum_a += int(i)

print(sum_a)