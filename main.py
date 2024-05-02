"""Goal: Run a bool function to check if an input number is prime"""


def get_input():
    n = int(input("Enter a positive integer: "))
    while n < 0:
        n = int(input("Enter a POSITIVE integer: "))

    # Edge case 2: user passes non integer value
    return n


def main():

    n = get_input()
    # is_prime(n)
    pass

    print(n)

    return 0


if __name__ == "__main__":
    main()
