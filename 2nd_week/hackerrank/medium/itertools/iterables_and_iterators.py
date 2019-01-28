# link to problem
# https://www.hackerrank.com/challenges/iterables-and-iterators/problem


from itertools import combinations

_,s,n = input(),input().split(),int(input())
t = list(combinations(s,n))
f = [i for i in t if 'a' in i]
print(len(f)/len(t))