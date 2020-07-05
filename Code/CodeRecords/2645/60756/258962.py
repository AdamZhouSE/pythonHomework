import math
plies=list(map(int,input()[1:-1].split(",")))
n=len(plies)
H=int(input())
L=0
R=max(plies)
K=0
while L<R:
    K=(L+R)//2+1
    time=sum(list(map(lambda x:math.ceil(x/K),plies)))
    if time<=H:
        if R==K:break
        R=K
    else:
        if L==K:break
        L=K
print(K)