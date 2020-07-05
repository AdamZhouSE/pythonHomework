map=[]
for i in range(0,4):
    a=list(input())
    a=[int(u) for u in a]
    map.append(a)

def func(i,j,count):
    if i<0 or j<0 or i>=4 or j>=5 or not map[i][j]==1:
        return
    map[i][j]=count
    func(i+1,j,count)
    func(i,j+1,count)
    func(i-1,j,count)
    func(i,j-1,count)

count=2
for i in range(0,4):
    for j in range(0,5):
        if map[i][j]==1:
            func(i,j,count)
            count+=1
re=0
for i in range(0,4):
    for j in range(0,5):
        if map[i][j]>re:
            re=map[i][j]
print(re-1)