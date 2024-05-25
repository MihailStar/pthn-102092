# 1
print("Ваши числа:", end=" ")
print(int(input()), ",", sep="", end=" ")
print(int(input()), end=" ")
print("и", int(input()), sep=" ")


# 2
numbers = input()

print(numbers[-1], numbers[0], numbers[1], sep="")


# 3
print(
    ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"][
        int(input()) % 7
    ]
)


# 4
from functools import reduce

numbers = [
    number for number in (int(digit) for digit in iter(input, "0")) if 0 < number < 31
]

print(0 if len(numbers) == 0 else reduce(lambda acc, number: acc * number, numbers, 1))


# 5
numbers = [int(digit) for digit in input().split()]
prev_number = numbers[0]
counter = 0

for i in range(1, len(numbers)):
    number = numbers[i]

    if (prev_number + number) % 5 == 0:
        counter += 1

    prev_number = number

print(counter)


# 6
from math import ceil, floor

n = int(input())
numbers = [float(input()) for _ in range(n)]

print(
    *(
        numbers[: int(len(numbers) / 2 - 1)] + numbers[int(len(numbers) / 2 + 1) :]
        if n % 2 == 0
        else numbers[: floor(len(numbers) / 2)] + numbers[ceil(len(numbers) / 2) :]
    )[::-1]
)


# 7
def is_not_oo(word: str) -> bool:
    length = len(word)
    prev_char = word[0]

    if length < 2:
        return True

    for index in range(1, len(word)):
        char = word[index]

        if prev_char == "o" and char == "o" or prev_char == "O" and char == "O":
            return False

        prev_char = char

    return True


words = input().split()

print(
    *map(
        lambda word: word[::-1],
        (word for word in words if len(word) < 6 and is_not_oo(word)),
    )
)
