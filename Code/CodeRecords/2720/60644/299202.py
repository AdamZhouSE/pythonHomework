def makeConnected(n, con):
        if len(con) < n - 1:
            return -1
        
        parent, res = list(range(n)), n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        for i, j in con:
            x, y = find(i), find(j)
            if x != y:
                parent[x] = y
                res -= 1
                
        return res - 1

    
n=int(input())
a=input()[2:].split('[')
for i in range(0,len(a)):
    a[i]=a[i][:-2].split(',')
    for j in range(0,2):
        a[i][j]=int(a[i][j])
print(makeConnected(n,a))