#TASK
# https://www.hackerrank.com/challenges/no-idea/problem


n, m  = list(input().split(" "))

set_n = list(input().split(" "))

a = set(input().split(" "))
b = set(input().split(" "))

happiness = 0
for number in set_n:
    if number in a:
        happiness += 1
    elif number in b:
        happiness -= 1

print(happiness)