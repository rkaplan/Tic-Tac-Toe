import random
from gameboard import GameBoard

def request_player_move(board):
    move = raw_input('Enter row, col (1-indexed, comma separated):\n')
    return map(lambda m: int(m) - 1, move.split(','))

def request_cpu_move(board):
    return random.choice(board.avail_moves())

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
        print board
        if board.is_player_turn():
            move = request_player_move(board)
        else:
            move = request_cpu_move(board)
        board.do_move(move)

    end_game(board)

def run():
    board = GameBoard()
    play(board)

if __name__ == '__main__':
    run()