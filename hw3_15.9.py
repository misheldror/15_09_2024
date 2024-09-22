
num: int = int(input("Enter a number: "))

for i in range(num +1):
    for i in range(1, i + 1):
        print(i, end=" ")
    print()
for i in range(num +1, 1, -1):
    for i in range(1, i - 1):
        print(i, end=" ")
    print()

# START

x: int = int(input("Enter a number: "))
stars: int = 1
spaces: int = x // 2

for stars in range(1, x + 2, 2):
    for _ in range(1, spaces + 1):
        print(" ", end=" ")
    for _ in range(1, stars + 1):
        print("*", end=" ")
    print()
    spaces -= 1