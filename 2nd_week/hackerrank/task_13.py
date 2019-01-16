
# You are given two sets, A and B. 
# Your job is to find whether set A is a subset of set B.

# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Input Format

# The first line will contain the number of test cases, T. 
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.

quantity_t = int(input())

for i in range(quantity_t):
    quantity_a = int(input())
    set_a = set(input().split(" "))
    
    quantity_b = int(input())
    set_b = set(input().split(" "))

    is_subset = False
    subset_items = 0
    for item in set_a:
        if item in set_b:
            subset_items += 1
        else: 
            break
    
    if subset_items == quantity_a:
        is_subset = True

    print(is_subset)