# 1
for i in range(3, 64, 4):
    print(i, end=" ")


# 2
n = int(input())

for i in range(1, 11):
    print(f"{n}*{i} = {n * i}")


# 3
a, b = map(int, (input(), input()))

if a < b:
    for i in range(a + 1 if a % 2 == 0 else a, b + 1, 2):
        print(i, end=" ")
else:
    for i in range(a - 1 if a % 2 == 0 else a, b - 1, -2):
        print(i, end=" ")


# 4
even_numbers = [
    number for number in (int(input()) for _ in range(int(input()))) if number % 2 == 0
]

print(sum(even_numbers) / len(even_numbers))


# 5
numbers = [
    int(digit)
    for digit in iter(input, "0")
    if len(digit) == 4
    and digit.startswith("-")
    or len(digit) == 3
    and not digit.startswith("-")
]

print(min(numbers) if len(numbers) else "NO")
