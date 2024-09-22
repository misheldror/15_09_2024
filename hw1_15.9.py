import random

name: str = str (input("Enter your name: "))
counter: int = 1

while counter < 4:
    name: str = str(input("Enter your name: "))
    counter += 1
print(random.choice([name]))