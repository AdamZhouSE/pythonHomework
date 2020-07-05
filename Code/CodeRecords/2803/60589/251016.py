nm=input().split(' ')
n=int(nm[0])
m=int(nm[1])
state=[False]*m
for i in range(n):
    on=input().split(' ')
    on=list(map(int,on))
    on.pop(0)
    for a in on:
        state[a-1]=True
if state==[True]*m:
    print('YES')
else:
    print('NO')