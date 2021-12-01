import math
import time
from player import HumanPlayer, ComputerPlayer , SuperComputerPlayer





class TickTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row)+' |')

    @staticmethod
    def print_board_num():
        number_board = [[str(i) for i in range(j*3+1 , (j+1)*3+1)] for j in range (3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+' |')


    def make_move(self, square, letter):
        if self.board[square]==' ':
            self.board[square]= letter
            if self.winner(square,letter):
                self.current_winner= letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3 :(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+(i*3)] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_square(self):
        return self.board.count(' ')
        
    def available_moves(self):
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        
        # return moves
        return [i for i, x in enumerate(self.board) if x == " "]

def play(game, x_player, o_player,print_game = True):
    if print_game:
        game.print_board_num()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square,letter):
            if print_game:
                print(f'{letter} makes amove to square {square+1}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                    ab = input("Press Enter to continue")
                return letter

            letter = 'O' if letter =='X' else 'X'
            time.sleep(1)


    if print_game:
        print("It's a tie! ")
        ab = input("Press Enter to continue")



if __name__ =="__main__":
    o_player = SuperComputerPlayer('O')
    x_player = HumanPlayer('X')
    t = TickTacToe()
    play(t, x_player, o_player, print_game=True)