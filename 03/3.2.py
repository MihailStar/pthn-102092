# 1
print(*reversed(input().split()))


# 2
print(
    *(
        n
        for i, n in enumerate(map(int, input().split()))
        if not (n % 2 == 0 and i % 2 == 1)
    )
)


# 3
digits = input().split()

print(*digits[1:], digits[0])


# 4
digits = input().split()
prev_digit = digits[0]
counter = 0

for i in range(1, len(digits)):
    digit = digits[i]

    if prev_digit == digit:
        counter += 1

    prev_digit = digit

print(counter)


# 5
digits = input().split()
last_index = len(digits) - 1

for i in range(last_index + 1):
    if digits[i] == digits[last_index - i]:
        continue
    print("NO")
    break
else:
    print("YES")
