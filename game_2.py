import random

def fun1(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    attempt_no = 4
    while guess != random_number and count < attempt_no:
        guess = int(input("try to guess the number : ".title()))
        if guess < random_number:
            print("too Low".upper())
        elif guess > random_number:
            print("Too High".upper())

        elif guess == random_number:
            print(f"you guess the ans {random_number} Correctly!!".title())
            quit()
        else:
            print("game over")
            quit()
        count += 1
        print(f"{attempt_no - count} Attempt left.")

fun1(3)
