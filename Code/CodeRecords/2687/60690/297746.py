t=int(input())
res=[]
for i in range(t):
    num=int(input())
    this=[]
    one=1
    two=2
    expo,expt=1,1
    
    while one<=num:
        this.append(one)
        one+=4**expo
        expo+=1
    while two<=num:
        this.append(two)
        two+=2*4**expt
        expt+=1
    this.sort()
    res.append(this)
for l in res:
    for i in range(len(l)-1):
        print(l[i],end=" ")
    print(l[-1])