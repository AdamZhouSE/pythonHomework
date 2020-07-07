t=int(input())
for i in range(t):
        n=list(map(int,input().split()))
    
        k=list(map(int,input().split()))
        s=0
        for i in k:
            if i%n[1]==0:
                s|=i
        print(s)
    