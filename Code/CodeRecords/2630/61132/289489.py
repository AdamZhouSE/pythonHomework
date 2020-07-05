def done(l,t):
    def swim(l, val, x, y):
        if l[x][y]==val:
            l[x][y]='x'
        else:
            return
        maxx=len(l)-1
        maxy=len(l[maxx])-1
        if l[maxx][maxy]=='x':
            return
        if x:
            swim(l,val,x-1,y)
        if x<maxx:
            swim(l,val,x+1,y)
        if y:
            swim(l,val,x,y-1)
        if y<len(l[x])-1:
            swim(l,val,x,y+1)
    s = [i[:] for i in l]
    swim(s,t,0,0)
    if s[len(s)-1][len(s[0])-1] == 'x':
        return True
    return False


l=eval(input())
t=0
while True:
    for i in l:
        for j,k in enumerate(i):
            if k<t:
                i[j]=t
    if done(l,l[0][0]):
        print(t)
        break
    t+=1