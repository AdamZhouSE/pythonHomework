class Solution(object):
    def s(matrix, target):
        if matrix ==[]:
            return False
        row,col = len(matrix),len(matrix[0])
        x,y=0,col-1
        while x<row and y>=0:
            if target < matrix[x][y]:
                y-=1
            elif target > matrix[x][y]:
                x+=num = int(input())
data =[]*num
le = 0
for i in range(0,num):
    a=input().split(",")
    data.append(a)
li = data[0]
leng = len(li)
target = int(input())
print(s(data,target))
           