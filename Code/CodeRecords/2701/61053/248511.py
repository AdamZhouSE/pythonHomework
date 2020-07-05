class chess_board:
    def __init__(self):
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
    def game_end(self):
        #check rows
        for i in range(0,3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
        #check coloums
        for i in range(0,3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        #check diagonal line
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False

string = input()
lst = []
move = []
flag = False
for x in string:
    if '0' <= x <= '9':
        lst.append(int(x))
        if flag:
            move.append(lst)
            lst = []
        flag = not flag
cb = chess_board()
a_turn = True
end = False
for m in move:
    if a_turn:
        cb.board[m[0]][m[1]] = 'a'
    else:
        cb.board[m[0]][m[1]] = 'b'
    if cb.game_end():
        end = True
        break
    a_turn = not a_turn
if end:
    if a_turn:
        print("A")
    else:
        print("B")
else:
    if len(move) == 9:
        print("Draw")
    else:
        print("Pending")