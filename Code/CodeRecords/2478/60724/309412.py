T=int(input())
for i in range(T):
    string=input().split(" ")
    A,B=int(string[0]),int(string[1])
    N=int(input())
    interval=B-A
    result=A
    while N>1:
        result+=interval
        N-=1
    print(result)