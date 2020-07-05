t=int(input())
for i in range(0,t):
    A,B,M=list(map(int,input().split()))
    counter=0
    for i in range(A,B+1):
        if i%M==0:
            counter+=1
    print(counter)