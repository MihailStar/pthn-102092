# 1
words = input().split()

print(words[1], words[0])


# 2
string = input()
vowels = 0
not_vowels = 0

for char in string.lower():
    if char == " ":
        continue

    if char in "aeiouy":
        vowels += 1
    else:
        not_vowels += 1

if vowels > not_vowels:
    print("A")
elif vowels < not_vowels:
    print("B")
else:
    print("=")


# 3
words = input().split()

print(*filter(lambda word: word[0].lower() != word[-1].lower(), words))


# 4
def countVowels(word: str) -> int:
    counter = 0

    for char in word.lower():
        if char in ("a", "e", "i", "o", "u", "y"):
            counter += 1

    return counter


words = input().split()

print(*filter(lambda word: len(word) > 4 and countVowels(word) > 1, words), sep="\n")


# 5
password = input()

if (
    len(password) > 7
    and all(
        "0" <= char <= "9" or "A" <= char <= "Z" or "a" <= char <= "z" or char == "_"
        for char in password
    )
    and any(char.islower() for char in password)
    and any(char.isupper() for char in password)
    and any(char.isdigit() for char in password)
):
    print("+")
else:
    print("-")
