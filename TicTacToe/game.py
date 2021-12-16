import time
from Player import HumanPlayer, ComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # making a 3x3 board/ a single list
        self.current_winner = None  # keep track of the winner

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod  # static because it doesnt relate to any specific board, we don't have to pass in a self
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')  # ????

    def available_moves(self):
        # shorthand for code below
        return [i for i, spot in enumerate(self.board) if spot == ' ']

        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     #  enumerate makes a list of tuples so that each value in a list now has a corresponding int key
        #     #  ['x','x','o'] --> [(0, 'x'),(1,'x'),(2,'o')]
        #     if spot == ' ':
        #         moves.append(i)  # we add the index of the empty space to the moves list
        # return moves

    def empty_squares(self):
        return ' ' in self.board  # boolean that just says if there are empty spots or not

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if move is valid, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_index = square // 3  # division
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        # only ways to win a diagonal is if the square index is an even number (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all these checks fail
        return False


def play(game, X_player, O_player, print_game=True):
    # returns the winner of the game! or None for a tie
    if print_game:
        game.print_board_nums()
        letter = 'X'  # starting letter
        # iterate while game still has empty squares
        while game.empty_squares():
            if letter == 'O':
                square = O_player.get_move(game)
            else:
                square = X_player.get_move(game)

            if game.make_move(square, letter):
                if print_game:
                    print(letter + f' makes a move to square {square}')
                    game.print_board()
                    print('')  # just empty line

                if game.current_winner:  # if current_winner is not set to None anymore
                    if print_game:
                        print(letter + ' wins')
                    return letter

                # after we made our move, we need to alternate letters
                letter = 'O' if letter == 'X' else 'X'  # shorthand

                # if letter == 'X':
                #     letter = 'O'
                # else:
                #     letter = 'X'

            #  a short break
            time.sleep(0.8)
    if print_game:
        print('It\'s a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
