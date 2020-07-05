class Solution:
    def validTicTacToe(board) -> bool:
        x_count = 0
        o_count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    x_count += 1
                if board[i][j] == 'O':
                    o_count += 1

        if x_count != o_count and x_count - 1 != o_count:
            return False;
        if x_count == o_count and Solution.win(board, 'X'):
            return False;
        if x_count - 1 == o_count and Solution.win(board, 'O'):
            return False;
        return True;

    def win(board, p):
        for i in range(3):
            if all(board[i][j] == p for j in range(3)): return True;
            if all(board[j][i] == p for j in range(3)): return True;
        if board[0][0] == board[1][1] == board[2][2] == p: return True;
        if board[0][2] == board[1][1] == board[2][0] == p: return True;
        return False;
if __name__=='__main__':
    board=input().split(",")
    print(Solution.validTicTacToe(board))