import sys
import copy

HUMAN = True
CPU   = False

# 1 = player wins, -1 = cpu wins
def search(board, depth, player):

    if board.has_won(HUMAN):
        return { 'move': None, 'score': 1 }
    elif board.has_won(CPU):
        return { 'move': None, 'score': -1 }
    elif board.is_full():
        return { 'move': None, 'score': 0 }
    elif depth == 0:
        raise Exception('Depth limit reached, that shouldnt be happening while testing!')
        # return { move: None, score: board.evaluate()}

    # The human's turn, who seeks to maximize the score
    if player:
        best = { 'move': None, 'score': -sys.maxsize }
        for move in board.avail_moves():
            newBoard = copy.deepcopy(board)
            newBoard.do_move(move)
            child = search(newBoard, depth - 1, not player)
            if child['score'] > best['score']:
                best['move'] = move
                best['score'] = child['score']
        return best

    # The CPU's turn, who seeks to minimize the score
    else:
        best = { 'move': None, 'score': sys.maxsize }
        for move in board.avail_moves():
            newBoard = copy.deepcopy(board)
            newBoard.do_move(move)
            child = search(newBoard, depth - 1, not player)
            if child['score'] < best['score']:
                best['move'] = move
                best['score'] = child['score']
        return best


def find_best_move(board):
    player = board.is_player_turn()
    max_depth = board.dimension * board.dimension - board.num_moves_made()
    return search(board, max_depth, player)['move']