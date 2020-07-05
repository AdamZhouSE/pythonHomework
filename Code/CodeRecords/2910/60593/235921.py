n=int(input())
flag=True
change=[0 for i in range(n)]
for i in range(n):
    w,h=map(int,input().split())
    if(i>0):
        if(w<=hp and h<=hp):
            hp=max(w,h)
        else:
            if(w<=hp):
                hp=w
            elif(h<=hp):
                hp=h
            else:
                flag=False
    else:
        hp=max(w,h)
print('YES'if flag else'NO')