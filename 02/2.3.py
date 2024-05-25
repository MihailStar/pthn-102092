# 1
input()

if input() == input():
    print("Вы зарегистрированы")
else:
    print("Пароли не совпадают")


# 2
login = "admin"
password = "p@$$w0rD"
inputed_logit = input()
inputed_password = input()

if login == inputed_logit:
    if password == inputed_password:
        print("Вы вошли в систему")
    else:
        print("Неверный пароль")
else:
    print("Пользователь с таким именем не зарегистрирован")


# 3
print("Да" if "1" in input() else "Нет")


# 4
a, b, c, x = (int(input()) for _ in range(4))

if a < x and b < x or b < x and c < x or c < x and a < x:
    print("Да")
else:
    print("Нет")


# 5
m = int(input())

if m in (12, 1, 2):
    print("Зима")
elif m >= 3 and m <= 5:
    print("Весна")
elif m >= 6 and m <= 8:
    print("Лето")
elif m >= 9 and m <= 11:
    print("Осень")
else:
    print("Неверный номер месяца")
