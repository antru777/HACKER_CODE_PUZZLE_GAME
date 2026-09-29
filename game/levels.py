from game.functions import show_status
from game.utils import add_score, remove_life, remove_hint, game_over


def level_1():
    print("\n========== LEVEL 1 ==========")
    print("PASSWORD VERIFICATION")

    answer = input("Enter password: ")

    if answer.lower() == "python":
        print("Correct! Access granted.")
        return True
    else:
        print("Wrong password.")
        return False


def level_2():
    print("\n========== LEVEL 2 ==========")
    print("NUMBER LOCK")

    answer = input("What is 15 + 25? ")

    if answer == "40":
        print("Correct! Number lock opened.")
        return True
    else:
        print("Wrong answer.")
        return False


def level_3():
    print("\n========== LEVEL 3 ==========")
    print("LOOP COUNTER")

    count = 0

    for i in range(1, 6):
        count += 1

    answer = input("How many times did the loop run? ")

    if answer == str(count):
        print("Correct!")
        return True
    else:
        print("Wrong answer.")
        return False


def level_4():
    print("\n========== LEVEL 4 ==========")
    print("FUNCTION LOCK")

    def secret_function():
        return "open"

    answer = input("What does the secret function return? ")

    if answer.lower() == secret_function():
        print("Correct!")
        return True
    else:
        print("Wrong answer.")
        return False


def level_5():
    print("\n========== LEVEL 5 ==========")
    print("STRING DECRYPTION")

    code = "HACKER"
    answer = input("What is the first three characters of HACKER? ")

    if answer.upper() == code[:3]:
        print("Correct! Code decrypted.")
        return True
    else:
        print("Wrong answer.")
        return False


def level_6():
    print("\n========== LEVEL 6 ==========")
    print("LIST SECURITY")

    numbers = [10, 25, 7, 40, 15]

    print("Security numbers:", numbers)

    answer = input("Enter the largest number: ")

    if answer == str(max(numbers)):
        print("Correct!")
        return True
    else:
        print("Wrong answer.")
        return False


def level_7():
    print("\n========== LEVEL 7 ==========")
    print("SET SECURITY")

    numbers = [1, 2, 2, 3, 3, 4]

    unique_numbers = set(numbers)

    print("Numbers:", numbers)

    answer = input("How many unique numbers are there? ")

    if answer == str(len(unique_numbers)):
        print("Correct!")
        return True
    else:
        print("Wrong answer.")
        return False


def level_8():
    print("\n========== LEVEL 8 ==========")
    print("LINEAR SEARCH")

    names = ["Aman", "Riya", "Rahul", "Neha", "Ankit"]

    print("Names:", names)

    answer = input("Enter the name you want to search: ")

    found = False

    for name in names:
        if name.lower() == answer.lower():
            found = True
            break

    if found:
        print("Name found!")
        return True
    else:
        print("Name not found.")
        return False


def level_9():
    print("\n========== LEVEL 9 ==========")
    print("BUBBLE SORT")

    numbers = [5, 2, 8, 1, 3]

    print("Original list:", numbers)

    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print("Sorted list:", numbers)

    answer = input("Enter the first number after sorting: ")

    if answer == str(numbers[0]):
        print("Correct!")
        return True
    else:
        print("Wrong answer.")
        return False


def level_10():
    print("\n========== LEVEL 10 ==========")
    print("MASTER HACKER")

    numbers = [10, 20, 30, 40, 50]

    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    print("Numbers:", numbers)

    answer = input("Enter the average: ")

    if answer == str(int(average)):
        print("Correct!")
        return True
    else:
        print("Wrong answer.")
        return False


def play_game():

    score = 0
    lives = 3
    hints = 3

    levels = [
        level_1,
        level_2,
        level_3,
        level_4,
        level_5,
        level_6,
        level_7,
        level_8,
        level_9,
        level_10
    ]

    print("\n================================")
    print("      GAME STARTED!")
    print("================================")

    for level in levels:

        show_status(score, lives, hints)

        result = level()

        if result:
            score = add_score(score, 10)
            print("You earned +10 points!")

        else:
            lives = remove_life(lives)
            print("You lost 1 life.")

        if game_over(lives):
            print("\n================================")
            print("          GAME OVER")
            print("================================")
            print("Final Score:", score)
            return

    print("\n================================")
    print("       CONGRATULATIONS!")
    print("       MASTER HACKER!")
    print("================================")
    print("Final Score:", score)