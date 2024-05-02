def get_input():
    n = int(input("Enter a positive integer: "))
    while n < 0:
        n = int(input("Enter a POSITIVE integer: "))

    # Edge case 2: user passes non integer value
    return n


def is_prime(n):
    # Handle base cases
    if n <= 1:
        return False
    if n == 2:
        return True

    # Handle even numbers
    if n % 2 == 0:
        return False

    # Divide n by every odd number from 3 to sqrt(n)
    for x in range(3, int(n**0.5), 2):
        result = n / x
        if result % 2 == 0:
            return False

    return True


def main():

    n = get_input()
    print(is_prime(n))

    return 0


if __name__ == "__main__":
    main()
