import random

x: int = random.randint (1, 100)

guess: int = int(input("Guess a number: "))

counter: int = 1

while guess != x and 0 < guess < 101:
    while guess < x:
        print("too small")
        counter += 1
        guess = int(input("Guess a number: "))
    while guess > x:
        print("too big")
        counter += 1
        guess = int(input("Guess a number: "))

if guess == x:
    print(f"BINGO! {counter} tries")