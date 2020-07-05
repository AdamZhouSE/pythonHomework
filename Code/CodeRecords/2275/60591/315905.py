class Solution(object):
    def cal(self,test):
        now = 1
        result1 = 0
        for m in test:
            result1 += now ^ m
            now = 1- now
        now = 0
        result2 = 0
        for m in test:
            result2 += now ^ m
            now = 1 - now
        if(result1 % 2 == 1 and result2 % 2 == 1):
            return -1
        elif(result1 % 2 == 1):
            return result2
        elif(result2 % 2 == 1):
            return result1
        return min(result1,result2)

    def check(self,board):
        lines = [board[0]]
        result = []
        for t in board:
            if (t == lines[0]):
                result.append(1)
            else:
                if (len(lines) == 1):
                    lines.append(t)
                else:
                    if (lines[1] != t):
                        return -1
                result.append(0)
        if(len(lines) == 1 and board != 1):
            return -1
        return self.cal(result)
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        reverseBoard = []
        for i in range(len(board)):
            temp = []
            for j in range(len(board)):
                temp.append(board[j][i])
            reverseBoard.append(temp)
        a = self.check(board)
        b = self.check(reverseBoard)
        if(a == -1 or b == -1):
            return -1
        else:
            result = a + b
            if(result % 2 == 1):
                return -1
            else:
                return int(result/2)