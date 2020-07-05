def f(s):
    count=0
    visited=[]
    current=[0]
    while len(visited)<len(s):
        count+=1
        visited+=current
        b=[]
        for k in current:
            t=find_adjacent(k,s)
            for l in t:
                if l not in visited :
                    b.append(l)
        current=b
    return count
                    
def find_adjacent(node,matrix):
    s=[]
    for i in range(len(matrix)):
        if matrix[node][i]!=0:
            s.append(i)
    return s
            
a=int(input().strip())
s=[[0]*a for i in range(a)]
for i in range(a-1):
    line=input().strip()
    x=int(line.split()[0])
    y=int(line.split()[1])
    s[x][y]=1
    s[y][x]=1
print(f(s))
  