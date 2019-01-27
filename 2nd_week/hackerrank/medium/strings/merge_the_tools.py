# Consider the following:
#
# A string, s, of length n where s = c0c1...cn-1.
# An integer, k, where k is a factor of n.
# We can split s into k/n subsegments where each subsegment, ti, consists of a contiguous
# block of k characters in s. Then, use each ti to create string  such that:
#
# The characters in ui are a subsequence of the characters in ti.
# Any repeat occurrence of a character is removed from the string such that
# each character in  occurs exactly once. In other words, if the character at
# some index j in ti occurs at a previous index < j in ti, then do not include the
# character in string ui.
# Given s and k, print n/k lines where each line i denotes string ui.

# https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(string, k):
    len_k = int(len(string) / k)
    letter_index = 0

    for i in range(1, len_k+1):
        t = string[letter_index: k*i]
        u = ""
        for letter in t:
            if letter not in u:
                u += letter

        print(u)

        letter_index += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)