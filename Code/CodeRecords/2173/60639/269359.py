def solution(n):
    if n==1:
        return 1
    else:
        return n*n

t=int(input())
for i in range(t):
    n=int(input())
    sum=0
    for i in range(1,n+1):
        sum+=solution(i)
    print(sum)
    