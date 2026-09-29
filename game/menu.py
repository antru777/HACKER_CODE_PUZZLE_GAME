from game.levels import play_game


def show_instructions():
    print("\n========== INSTRUCTIONS ==========")
    print("1. There are 10 levels in the game.")
    print("2. You have 3 lives.")
    print("3. You have 3 hints.")
    print("4. Correct answer = +10 points.")
    print("5. Wrong answer = -1 life.")
    print("6. Using hint = -3 points.")
    print("7. Complete all levels to become a Master Hacker.")
    print("==================================\n")


def show_menu():
    while True:
        print("\n==============================")
        print("   HACKER CODE PUZZLE GAME")
        print("==============================")
        print("1. Start Game")
        print("2. Instructions")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()

        elif choice == "2":
            show_instructions()

        elif choice == "3":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please try again.")