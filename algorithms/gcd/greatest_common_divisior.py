def gcd1(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == b % d == 0:
            return d


def gcd2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def gcd3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)


def gcd4(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd4(b % a, a)
#
# def euclidGCD(a, b):
#
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     elif a >= b:
#         return euclidGCD(a%b, b)
#     elif b > a:
#         return euclidGCD(b%a, a)
#
#
# if __name__ == '__main__':
#
#     print(euclidGCD(2, 9))

