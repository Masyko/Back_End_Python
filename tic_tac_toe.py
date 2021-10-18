""" Task 1"""
board = list(range(1, 10))
wins_combo = [(1, 2, 3),
              (1, 4, 7),
              (4, 5, 6),
              (7, 8, 9),
              (2, 5, 8),
              (3, 6, 9),
              (1, 5, 9),
              (3, 5, 7)]


def draw_board():
    """" Function to draw playing board """
    print('_____________')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def take_input(player_sign):
    """ Function to take which place was chousen by player """
    while True:
        value = input('Куда вы хотите поставить ' + player_sign + ' ? ')
        if not value in '123456789':
            print('Этой клетки не существует! Попробуйте выбрать другую из представленных')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XxOo0хХоО':
            print('Данная клетка уже занята')
            continue
        board[value - 1] = player_sign
        break


def check_win(board_w):
    """ Function to check win """
    for each in wins_combo:
        if (board_w[each[0] - 1]) == (board_w[each[1] - 1]) == (board_w[each[2] - 1]):
            return board_w[each[1] - 1]
    return False


def main():
    """ Main function """
    counter = 0
    print('Hello players, Welcome in our "Крестики/Нолики" game!')
    print('Пожалуйста, введите ваши имена')
    while True:
        player_1 = input('Введите имя первого игрока: ')
        if player_1 in ' ' or (len(player_1) > 20):
            print('Вы некорректно ввели имя, поробуйт еще раз и не слишком длинно :)')
            continue
        break
    while True:
        player_2 = input('Введите имя второго игрока: ')
        if player_2 in ' ' or (len(player_2) > 20):
            print('Вы некорректно ввели имя, поробуйт еще раз и не слишком длинно :)')
            continue
        break
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
            winner = player_1
        else:
            take_input('O')
            winner = player_2
        if counter > 3:
            win = check_win(board)
            if win:
                draw_board()
                print('Выиграл игрок', winner, 'Поздравляем!')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Победила дружба! Ничья')
            break


main()
