def merge_the_tools(string, k):
    len_k = len(string) - k
    letter_index = 0

    for i in range(1, len_k+1):
        t = string[letter_index: k*i]
        u = ""
        for letter in t:
            if letter not in u:
                u += letter

        print(u)

        letter_index += k
