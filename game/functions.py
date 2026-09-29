def show_status(score, lives, hints):
    print("\n--------------------------")
    print("Score :", score)
    print("Lives :", lives)
    print("Hints :", hints)
    print("--------------------------")


def use_hint(hint):
    print("\nHINT:", hint)


def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()