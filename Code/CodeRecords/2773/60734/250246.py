import re

class Solution:
    def __init__(self,matrix):
        self.matrix = matrix
        self.maxlen = 0
        self.visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]

    def move(self,row,col,curlen):
        curNum = self.matrix[row][col]
        self.visited[row][col] = True
        curlen+=1
        if curlen>self.maxlen:
            self.maxlen = curlen
        
        #上
        if row-1>=0 and self.matrix[row-1][col]>curNum\
        and self.visited[row-1][col]==False:
            self.move(row-1,col,curlen)
        #下
        if row+1<len(self.matrix[0]) and self.matrix[row+1][col]>curNum\
        and self.visited[row+1][col]==False:
            self.move(row+1,col,curlen)
        #左
        if col-1>=0 and self.matrix[row][col-1]>curNum\
        and self.visited[row][col-1]==False:
            self.move(row,col-1,curlen)
        #右
        if col+1<len(self.matrix) and self.matrix[row][col+1]>curNum\
        and self.visited[row][col+1]==False:
            self.move(row,col+1,curlen)
        
        #还原
        self.visited[row][col] = False
        curlen-=1
        
    def longestPath(self):
        if len(self.matrix) == 0:
            self.maxlen = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.move(i,j,0)

if __name__ == "__main__":
    #输入
    matrix = []
    for line in iter(input,']'):
        lst = re.findall(r'\d+',line)
        if len(lst)>0:
            matrix.append(list(map(int,lst)))

    solution = Solution(matrix)
    solution.longestPath()
    print(solution.maxlen)