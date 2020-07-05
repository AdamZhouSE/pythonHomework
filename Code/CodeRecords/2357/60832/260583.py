All = int(input())

for q in range(0, All):
    temp=input().split()
    n=int(temp[0])
    m=int(temp[1])
    x=int(temp[2])
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    for t in A:
        if x-t in B:
            print(t,x-t)