def done(l,t):
    def swim(l, val, x, y):
        if l[x][y]==val:
            l[x][y]=0
        else:
            return
        if x:
            swim(l,val,x-1,y)
        if x<len(l)-1:
            swim(l,val,x+1,y)
        if y:
            swim(l,val,x,y-1)
        if y<len(l[x])-1:
            swim(l,val,x,y+1)
    s = [i[:] for i in l]
    sum=0
    for i in range(len(l)):
        for j in range(len(l[0])):
            if s[i][j]==1:
                sum+=1
                swim(s, 1, i, j)
    return sum

l=[]
for i in range(4):
    l.append(list(map(int,list(input()))))
print(done(l,1))