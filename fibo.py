def recursive_nth_fibo(n):
    # uprava i s nulou na zacatku
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1

    if n <= 1:
        return 1

    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)


def main():
    number = int(input("Kolik prvku FS chces: "))
    fs = [recursive_nth_fibo(n) for n in range(number)]
    # fs = recursive_nth_fibo(number)
    print(fs)
    pass


if __name__ == '__main__':
    main()
