m=int(input())
n=int(input())
k=int(input())
table=[[-1]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        table[i][j]=(i+1)*(j+1)

def findMin():
    temp=m*n
    x=m-1
    y=n-1
    for i in range(m):
        for j in range(n):
            if(table[i][j]<temp):
                temp=table[i][j]
                x=i
                y=j
    table[x][y]=m*n
    return temp
            
for i in range(k):
    mini=findMin()
    
print(mini)
