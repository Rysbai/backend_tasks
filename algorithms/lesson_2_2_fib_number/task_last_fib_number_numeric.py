

def fib_digit(n):
    f = list(range(n + 1))

    for i in range(2, n + 1):
        f[i] = int(str(f[i - 1] + f[i - 2])[-1])

    return f[n]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
