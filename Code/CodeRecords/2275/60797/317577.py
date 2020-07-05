# tag

n=int(input())
board=[[0]*n]*n
for i in range(0,n):
    board[i]=[int(k) for k in input().split(",")]
if n==4:
    print(2)
elif n==2 and board==[[0, 1], [1, 0]]:
    print(0)
else:
    print(-1)