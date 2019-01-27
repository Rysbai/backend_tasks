
# TASK
# https://www.hackerrank.com/challenges/find-angle/problem

import math
a = float(input())
b = float(input())

print(str(int(round(math.degrees(math.atan2(a, b)))))+'°')