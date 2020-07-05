def count():
    N=int(input())
    l=list(map(int,input().split()))
    count=0
    for i in range(0,N-1):
        for j in range (i+1,N):
            if l[i]>l[j]:
                count+=1
    return count                
    
    
T=int(input())
for i in range(0,T):
    print(count())