n=int(input())
flag=True
for i in range(n):
    wa,ha=map(int,input().split())
    if(i>0):
        if(wa<wp and ha<hp and wa<hp and ha<wp):
            flag=False
    wp=wa
    hp=ha
print('YES'if flag else'NO')