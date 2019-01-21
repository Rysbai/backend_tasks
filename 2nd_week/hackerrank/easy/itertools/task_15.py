# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = list(input().split(" "))
b = list(input().split(" "))
list_a = []
list_b = []

for number in a:
    list_a.append(int(number))

for number in b:
    list_b.append(int(number))


product_of_lists_a_and_b = ""

for item in product(list_a, list_b):
    product_of_lists_a_and_b += str(item) + " "

print(product_of_lists_a_and_b)

