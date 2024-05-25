# 1
from functools import reduce

digits = [int(digit) for digit in input()]

a = digits.count(digits[-1])

b_digits = [digit for digit in digits if digit > 5]
b = -1 if len(b_digits) == 0 else reduce(lambda acc, digit: acc + digit, b_digits, 0)

v_digits = [digit for digit in digits if digit < 7]
v = -1 if len(v_digits) == 0 else reduce(lambda acc, digit: acc * digit, v_digits, 1)

print(f"а) {a}")
print(f"б) {b}")
print(f"в) {v}")


# 2
digits = [int(digit) for digit in input()]

print(f"Максимальная: {digits.index(max(digits)) + 1}")
print(f"Минимальная: {digits.index(min(digits)) + 1}")


# 3
from math import gcd

a, b = map(int, (input(), input()))

print(int((a * b) / gcd(a, b)))


# 4
numbers = [int(input()) for _index in range(int(input()))]

for index, number in enumerate(numbers):
    if str(number).endswith("7"):
        print(f"а) {index + 1}")
        break
else:
    print("а) NO")

print(f"б) {min(numbers)}")
print(f"в) {sum(number for number in numbers if number % 3 == 0 and number % 4 != 0)}")


# 5
numbers = [int(digit) for digit in iter(input, "0")]
a_numbers = [
    number
    for number in numbers
    if len(str(number)) == 2 and not str(number).startswith("-")
]

if len(a_numbers) == 0:
    print("а) 0")
else:
    print(f"а) {sum(a_numbers) / len(a_numbers)}")


print(f"б) {max(numbers)}")
print(f"в) {len([number for number in numbers if number % 2 == 1])}")
