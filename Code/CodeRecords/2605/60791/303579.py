N,M = [int(i) for i in input().split(' ')]
a =  [[int(i)] for i in input().split(' ')]

index = [0]*N
for i in range(N):
    index[i] = i;

for i in range(M):
    behave =  [int(i) for i in input().split(' ')]
    
    if behave[0] == 1:
        
        x,y = behave[1]-1,behave[2]-1
        while index[x] != x:
            x = index[x]
        while index[y] != y:
            y = index[y]
        big = max(x,y)
        mini = min(x,y)
        
        
        a[index[mini]]+=a[index[big]]
        a[index[mini]].sort(reverse = True)
        index[big] = index[mini]
    else:
        
        tar = behave[1]-1
        while tar != index[tar]:
            tar = index[tar]
        print(a[index[tar]][-1])
        a[index[tar-1]].pop()
        
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        