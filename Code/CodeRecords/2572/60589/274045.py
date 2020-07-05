lto=input().split(' ')
l=int(lto[0])
t=int(lto[1])
o=int(lto[2])
board= [1] * l
for i in range(o):
    action=input().split(' ')
    op=action[0]
    if op=='C':
        a=int(action[1])
        b=int(action[2])
        c=int(action[3])
        for i in range(a-1,b):
            board[i]=c
    else:
        a = int(action[1])
        b = int(action[2])
        ans=set();
        for i in range(a - 1, b):
            ans.add(board[i])
        print(len(ans))