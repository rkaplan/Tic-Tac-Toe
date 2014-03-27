class GameBoard():
    def __init__(self, dimension=3, playerStart=True):
        self.dimension = dimension
        self.grid = [['-' for col in range(dimension)] for row in range(dimension)]
        self.playerStart = playerStart
        self.playerTurn = playerStart
        self.moves_made = 0

    def __repr__(self):
        return '\n'.join([''.join(row) for row in self.grid])

    def __getitem__(self, index):
        return self.grid[index]

    def __setitem__(self, index, value):
        self.grid[index] = value

    def do_move(self, move):
        r, c = move
        if self.playerTurn:
            self.grid[r][c] = 'X'
        else:
            self.grid[r][c] = 'O'
        self.playerTurn = not self.playerTurn
        self.moves_made += 1

    def num_moves_made(self):
        return self.moves_made

    def is_player_turn(self):
        return self.playerTurn

    def is_finished(self):
        return self.get_winner() is not None or self.is_full()

    def get_winner(self):
        if self.has_symbol_won('X'):
            return 'X'
        if self.has_symbol_won('O'):
            return 'O'
        return None

    def has_won(self, player):
        return self.has_symbol_won(self.translate(player))

    def has_symbol_won(self, symbol):
        return self.has_symbol_won_row(symbol) or self.has_symbol_won_col(symbol) or self.has_symbol_won_diag(symbol)

    def has_symbol_won_row(self, symbol):
        for row in self.grid:
            if symbol * self.dimension == ''.join(row):
                return True
        return False

    def has_symbol_won_col(self, symbol):
        for c in range(self.dimension):
            if symbol * self.dimension == ''.join([self.grid[r][c] for r in range(self.dimension)]):
                return True
        return False

    def has_symbol_won_diag(self, symbol):
        if symbol * self.dimension == ''.join([self.grid[i][i] for i in range(self.dimension)]):
            return True
        if symbol * self.dimension == ''.join([self.grid[i][self.dimension - i - 1] for i in range(self.dimension)]):
            return True
        return False

    def is_full(self):
        return self.moves_made == self.dimension * self.dimension

    def avail_moves(self):
        return [(r, c) for c in range(self.dimension) for r in range(self.dimension) if self.grid[r][c] == '-']

    def evaluate(self):
        """The heuristic function to statically evaluate the board"""
        return 0 # TODO: implement

    def translate(self, player):
        if self.playerStart == player:
            return 'X'
        else:
            return 'O'
