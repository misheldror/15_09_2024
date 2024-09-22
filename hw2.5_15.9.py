
t: float = 0
s: int = 0
counter: int = 0

while counter < 5:
    if -50 <= t <= 45:
        t: float = float (input("enter temperature: "))
        s += t
        counter += 1
    else:
        print(f"{t} is incorrect")
        t: float = float(input("enter temperature: "))
av = s / 5
print(av)