# Trial-division
This simple Python program checks whether a given positive integer is a prime number using trial division

## Description
The program consists of three main functions:

- `get_input()`: Prompts the user to enter a positive integer. It ensures the input is valid and positive through a loop that continues until the input meets the conditions.

- `is_prime(n)`: Determines if the given number `n` is a prime. The function handles base cases (e.g., n <= 1 and n == 2), checks even numbers, and divides `n` by every odd number up to the square root of `n`.

- `main()`: Controls the flow of the program, calling `get_input()` to retrieve the user's number and `is_prime()` to check its primality. The result is then printed.

## How to Run

1. Ensure you have Python installed on your computer
2. Save the script in a file, for example `prime_checker.py`
3. Open a terminal or command prompt
4. Navigate to the directory where the script is saved
5. Run the script using the command:

```bash
python trial_division.py
```
6. Follow the on-screen prompts to input a positive integer

The script will then output whether the entered number is prime or not.

## Features
- Input validation to only accept positive integers
- Efficient primality testing using trial division up to the square root of the input number

Feel free to modify and use this code as part of your own projects!
