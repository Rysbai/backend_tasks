
#TASK
# Read an integer N.
# Without using any string methods, try to print the following:
# Note that "" represents the values in between.
#input >>>3
#output >>>123


n = int(input())

num = ''
for i in range(1, n+1):
    num += str(i)

print(num)