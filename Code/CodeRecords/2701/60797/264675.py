class Solution:
    def tictactoe(self, moves) -> str:
        '''
        board = [[" "] * 4] * 4
        board[0][1] = "1"
        board[0][2] = "2"
        board[0][3] = "3"
        board[1][0] = "1"
        board[2][0] = "2"
        board[3][0] = "3"
        '''
        board = [[" "] * 3 for i in range(3)]
        who = "X"
        for i, j in moves:
            board[i][j] = who
            if who == "X":
                who = "O"
            else:
                who = "X"
            if self.judge(board) == "X":
                return "A"
            elif self.judge(board) == "O":
                return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"

    def judge(self, board) -> str:
        for i in range(0, 3):
            sign = 0
            for j in range(0, 3):
                if board[i][j] == "X":
                    sign += 1
                if board[i][j] == "O":
                    sign -= 1
            if sign == 3:
                return "X"
            elif sign == -3:
                return "O"
        for j in range(0, 3):
            sign = 0
            for i in range(0, 3):
                if board[i][j] == "X":
                    sign += 1
                if board[i][j] == "O":
                    sign -= 1
            if sign == 3:
                return "X"
            elif sign == -3:
                return "O"
        if board[1][1] == "X" and (
                (board[0][0] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[2][0] == "X")):
            return "X"
        elif board[1][1] == "O" and (
                (board[0][0] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[2][0] == "O")):
            return "O"

if __name__ == "__main__":
    data = [[int(a) for a in item.strip('[]').split(',')] for item in input().split('],[')]
    s = Solution()
    re = s.tictactoe(data)
    print(re)