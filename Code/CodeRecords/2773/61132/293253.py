def done(l):
    def swim(l, x, y):
        val1=val2=val3=val4=0
        if x and l[x-1][y]>l[x][y]:
            val1=swim(l,x-1,y)
        if x<len(l)-1 and l[x+1][y]>l[x][y]:
            val2=swim(l,x+1,y)
        if y and l[x][y-1]>l[x][y]:
            val3=swim(l,x,y-1)
        if y<len(l[x])-1 and l[x][y+1]>l[x][y]:
            val4=swim(l,x,y+1)
        return 1+max(val1,val2,val3,val4)
    Max=1
    s = [i[:] for i in l]
    for i in range(len(l)):
        for j in range(len(l[0])):
            Max=max(Max,swim(s,i,j))
    return Max

if input()=='[':
    l=[]
    while True:
        tmp=input()
        if tmp==']':
            break
        if tmp[-1]==',':
            tmp=tmp[:-1]
        l.append(eval(tmp))
else:
    print("Wrong")
print(done(l))