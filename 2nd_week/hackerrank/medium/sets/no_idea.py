#TASK
# https://www.hackerrank.com/challenges/no-idea/problem


integers = list(input().split(" "))
n = int(integers[0])
m = int(integers[1])

array_n = list(input().split(" "))

a = set(input().split(" "))
b = set(input().split(" "))

happiness = 0
set_n = []
for number in array_n:
    if number not in set_n:
        if number in a:
            happiness += 1
            set_n.append(number)
        else:
            happiness -= 1
            set_n.append(number)

print(happiness)