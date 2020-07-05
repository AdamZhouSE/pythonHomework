n=int(input())
ls=[]
for i in range(n):
    m=input()
    l=[]
    for j in range(n):
        l.append(m[i])
    ls.append(l)
total=0
for i in range(n):
    for j in range(n):#现在是ls[i][j]
        
        