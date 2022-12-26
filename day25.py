from math import ceil, floor, log

with open("input.txt") as f:
    lines = f.readlines()


def snafu_to_number(snafu: str) -> int:
    total = 0

    for i, c in enumerate(snafu[::-1]):
        if c.isnumeric():
            total += int(c) * 5**i
        if c == "-":
            total -= 5**i
        if c == "=":
            total -= 5**i * 2

    return total


def number_to_snafu(number: int) -> str:
    res = ""
    while number > 0:
        res += "012=-"[number % 5]
        if number >= 3:
            number += 2
        number = number // 5

    return res[::-1]


number = sum(snafu_to_number(line.strip()) for line in lines)
print(number_to_snafu(number))
