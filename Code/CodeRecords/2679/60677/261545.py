times=int(input())
for i in range(times):
    n=int(input())
    answer=0
    if n==1:
        answer=3
    elif n==2:
        answer=8
    else:
        answer=1+n+n+n*(n-1)+n*(n-1)/2+n*(n-1)*(n-2)/2
    print(int(answer))