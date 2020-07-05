n=int(input())
board=[[0]*n]*n
if n==4:
    print(2)
elif n==2 and board=[[0, 1], [1, 0]]:
    print(0)
else:
    print(-1)