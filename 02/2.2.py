# 1
a, b = map(int, input().split())

print(f"{a} + {b} = {a + b}")


# 2
print(eval("*".join(list(input()))))


# 3
print(("".join(reversed(list(input())))))


# 4
n = int(input())
temp = n
s = temp % 60
temp //= 60
m = temp % 60
temp //= 60
h = temp % 24

# :fill align sign # 0 width sep .precision type
# :0 width
# @tutorial https://cheatography.com/brianallan/cheat-sheets/python-f-strings-number-formatting

print(f"{h:02}:{m:02}:{s:02}")


# 5
a, b = input(), input()

print((int(f"{a[0]}{b[0]}") + int(f"{a[1]}{b[1]}") + int(f"{a[2]}{b[2]}")) ** 0.5)
