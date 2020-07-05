n=int(input())
w,h=map(int,input().split(' '))
index=max(w,h)
flag=1
for i in range(n-1):
    w,h=map(int,input().split(' '))
    if index>=max(w,h):
        index=max(w,h)
    elif index>=min(w,h):
        index=min(w,h)
    else:
        flag=0
if flag:
    print('YES')
else:
    print('NO')
        
    
