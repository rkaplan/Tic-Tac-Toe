import random
import gameboard
import ai

def string_to_move(move_str):
    return map(lambda m: int(m) - 1, move_str.split(','))

def move_to_string(move):
    return "{}, {}".format(*map(lambda m: m + 1, move))

def request_player_move(board):
    move_str = raw_input('Enter row, col (1-indexed, comma separated): ')
    return string_to_move(move_str)

def request_cpu_move(board):
    return ai.find_best_move(board)

def end_game(board):
    print board
    winner = board.get_winner()
    if winner == 'X':
        print 'Congratulations, you won!'
    elif winner == 'O':
        print 'You lost. Better luck next time.'
    else:
        print 'It\'s a tie!'

def play(board):
    while not board.is_finished():
        print board, '\n'
        if board.is_player_turn():
            move = request_player_move(board)
            print 'You moved', move_to_string(move)
        else:
            move = request_cpu_move(board)
            print 'CPU moved', move_to_string(move)
        board.do_move(move)

    end_game(board)

def run():
    board = gameboard.GameBoard()
    play(board)

if __name__ == '__main__':
    run()