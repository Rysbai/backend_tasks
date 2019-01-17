
# TASK
# You are given a set A and n other sets. 
# Your job is to find whether set A is a strict superset of each of the n sets.

# Print True, if A is a strict superset of each of the n sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

set_a = set(input().split(" "))
next_sets_quantity = int(input())

supersets_quantity = 0
for i in range(next_sets_quantity):
    set_n = set(input().split(" "))
    if set_a.issuperset(set_n) and len(set_a) > len(set_n):
        supersets_quantity += 1

if next_sets_quantity == supersets_quantity:
    print(True)
else:
    print(False)