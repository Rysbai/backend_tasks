# TASK
# In this task, we would like for you to appreciate the usefulness of the groupby() function 
# of itertools . To read more about this function, Check this out .

# You are given a string S. Suppose a character 'c' 
# occurs consecutively X times in the string. Replace these consecutive occurrences of 
# the character 'c' with (X, c) in the string.


from itertools import groupby

string = input()
def get_group_list(string):
    group_list = []
    index = 0
    flag = True
    group = string[index]
    for i in range(len(string)):
        item = string[index]
        if item == string[index + 1]:
            group += string[index + 1]
            index += 1
        else:
            index = len(group)
            group_list.append(group)
            group = string[index]


    return group_list
# a = []
# count = 0
# pre = ''
# for i in string:
#     try:
#         if a[count][1] != i or pre == i:
#             a[count][0] += 1
#         else:
#             a.append((0, i))
#     except:
#         pass
#     count += 1
#     pre = 1
group_list = get_group_list(string)
        
result = groupby(group_list, lambda x: len(x))
for key, value in list(result):
    value = list(value)
    print(key, value)