import random

print("Welcome to DICE GAME!")

i = ""
scr = 0  # Score
count = 0

while i != "n":
    x = int(input("Enter Number from (1-6): "))
    y = random.randint(1, 6)

    if x not in range(1, 6 + 1):
        print("Number must be between 1 to 6!")
    else:
        print(f"({x}, {y})")
        if x == y:
            scr += 1

    if count >= 5:
        i = str(input("Do you want to continue?"
                      " (Y/n): "))
    count += 1

print("Game Over!")
print("Your Score:", scr)
