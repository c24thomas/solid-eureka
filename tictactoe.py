blank_board = [['-' for _ in range(3)] for _ in range(3)]


class InvalidMove(Exception):
    pass


class TicTacToe:

    def __init__(self):

        self.board = blank_board
        self.game_is_on = True
        self.player = 'x'
        self.moves = []

    def print_board(self):
        print(f'  {self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}  \n'
              f'-----|-----|-----\n'
              f'  {self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}  \n'
              f'-----|-----|-----\n'
              f'  {self.board[2][0]}  |  {self.board[2][1]}  |  {self.board[2][2]}  \n'
              )
        print('Possible moves (left to right, top to bottom):')

    def make_move(self, move, player):
        if move not in range(1, 10):
            raise InvalidMove
        row = (move - 1) // 3
        col = (move - 1) % 3
        if self.board[row][col] == '-':
            self.board[row][col] = player
        else:
            raise InvalidMove

    # Check which squares contain '-', denoting an empty space (possible move)
    def get_moves(self):
        self.moves = []
        squares_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for row_idx, row in enumerate(self.board):
            for col_idx, col in enumerate(row):
                if col == '-':
                    self.moves.append(squares_list[row_idx][col_idx])
        if len(self.moves) == 0:
            self.game_over()
        return self.moves

    def new_game(self):
        self.board = blank_board

    def has_won(self, player):
        for row in self.board:
            # 3 across
            if row.count(player) == 3:
                return True
            else:
                return False
        # 3 vertical (left)
        if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True
        # 3 vertical (center)
        elif self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
            return True
        # 3 vertical (right)
        elif self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
            return True
        # Diagonal top left to bottom right
        elif self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        # Diagonal bottom left to top right
        elif self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        else:
            return False

    def switch(self):
        if self.player == 'x':
            self.player = 'o'
        else:
            self.player = 'x'

    def game_over(self):
        self.game_is_on = False
        self.print_board()
        if self.has_won('x'):
            print('X wins!')
        elif self.has_won('o'):
            print('O wins!')
        else:
            print('It\'s a tie!')
        again = input('Would you like to play again? (y/n)\n')
        if again == 'y':
            self.play()

    def play(self):
        self.game_is_on = True
        self.new_game()
        self.moves = []
        while self.game_is_on:
            self.print_board()
            print(self.get_moves())
            print(f'{self.player.upper()}\'s turn.')
            choice = int(input('Where would you like to move?\n'))
            try:
                self.make_move(choice, self.player)
            except InvalidMove:
                print('Invalid move. Try again.')
                pass
            else:
                if self.has_won(self.player):
                    self.game_over()
                else:
                    self.switch()
        self.game_over()
