def create_fizz_buzz_list(n):
    fizz_buzz_list = []
    for i in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            fizz_buzz_list.append("FizzBuzz")
        elif n % 3 == 0:
            fizz_buzz_list.append("Fizz")
        elif n % 5 == 0:
            fizz_buzz_list.append("Buzz")
        else:
            fizz_buzz_list.append(i)
    return fizz_buzz_list


def translate_letter_to_numbers(string):
    if not 1 < len(string) <= 30:
        raise ValueError("Expression with invalid length")
    number = ""

    for char in string:
        if char in "ABC":
            number += "2"
        elif char in "DEF":
            number += "3"
        elif char in "GHI":
            number += "4"
        elif char in "JKL":
            number += "5"
        elif char in "MNO":
            number += "6"
        elif char in "PQRS":
            number += "7"
        elif char in "TUV":
            number += "8"
        elif char in "WXYZ":
            number += "9"
        elif char in "-01":
            number += char
        else:
            raise ValueError("Invalid character")

    return number
