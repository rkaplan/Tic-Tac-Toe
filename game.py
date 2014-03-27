import random
from gameboard import GameBoard

def request_player_move(board):
    print board
    move = raw_input('Enter row, col (1-indexed, comma separated):\n')
    return map(lambda m: int(m) - 1, move.split(','))

def request_cpu_move(board):
    return random.choice(board.avail_moves())

def play(board):
    while not board.is_finished():
        if board.playerTurn:
            move = request_player_move(board)
        else:
            move = request_cpu_move(board)
        board.do_move(move)

def run():
    board = GameBoard()
    play(board)

if __name__ == '__main__':
    run()