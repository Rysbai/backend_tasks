

def choose_applications1(S):
    solution = []
    while S:
        S = sorted(S)
        min_res = S[0]
        solution.append(min_res)

        S.remove(min_res)
        for interval in S:
            if interval[0] < min_res[1]:
                S.remove(interval)
            else:
                break

    return solution


print(choose_applications1([[2, 3], [0.5, 2.5], [2, 3]]))
