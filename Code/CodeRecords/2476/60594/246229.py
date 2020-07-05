n=(int)(input())
for index in range(n):
    n=(int)(input())
    A=input().split()
    now=[]
    for index in range(len(A)):
        now.append((int)(A[index]))
    zongfei=0
    while len(now)!=1:
        now.sort()
        zongfei+=now[0]+now[1]
        now.append(now[0]+now[1])
        now.pop(0)
        now.pop(0)
    print(zongfei)