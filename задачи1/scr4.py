import random
def play_game():
    print("камень, ножницы или бумага ?")
    moves = ["камень", "ножницы", "бумага"]
    while True:
        user_move = input("Выберите: ").lower()
        if user_move not in moves:
            print("Некорректный ввод. Попробуйте ещё раз.")
            continue
        computer_move = random.choice(moves)
        print(f"соперник выбрал: {computer_move}")
        if user_move == computer_move:
            print("Ничья")
        elif (user_move == "камень" and computer_move == "ножницы") or \
             (user_move == "ножницы" and computer_move == "бумага") or \
             (user_move == "бумага" and computer_move == "камень"):
            print("победа!")
        else:
            print("Компьютер победил(((")
        play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break
play_game()