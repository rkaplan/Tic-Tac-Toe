class GameBoard():
    def __init__(self, dimension=3, playerStart=True):
        self.dimension = dimension
        self.grid = [['-' for col in range(dimension)] for row in range(dimension)]
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

    def is_player_turn(self):
        return self.playerTurn

    def is_finished(self):
        return self.get_winner() is not None or self.is_full()

    def get_winner(self):
        if self.has_won('X'):
            return 'X'
        if self.has_won('O'):
            return 'O'
        return None

    def has_won(self, player):
        return self.has_won_row(player) or self.has_won_col(player) or self.has_won_diag(player)

    def has_won_row(self, player):
        for row in self.grid:
            if player * self.dimension == ''.join(row):
                return True
        return False

    def has_won_col(self, player):
        for c in range(self.dimension):
            if player * self.dimension == ''.join([self.grid[r][c] for r in range(self.dimension)]):
                return True
        return False

    def has_won_diag(self, player):
        if player * self.dimension == ''.join([self.grid[i][i] for i in range(self.dimension)]):
            return True
        if player * self.dimension == ''.join([self.grid[i][self.dimension - i - 1] for i in range(self.dimension)]):
            return True
        return False

    def is_full(self):
        return self.moves_made == self.dimension * self.dimension

    def avail_moves(self):
        return [(r, c) for c in range(self.dimension) for r in range(self.dimension) if self.grid[r][c] == '-']
