class plan:
    def __init__(self,l,r):
        self.l=l
        self.r=r
    def __lt__(self, value):
        return self.r<value.l
    def __gt__(self,value):
        return self.l>value.r
n=int(input())
s=set()
for t in range(n):
    a=list(input().split())
    if(a[0]=='A'):
        l,r=a[1],a[2]
        tmp=plan(l,r)
        cnt=0
        for i in list(s):
            if(not tmp<i and not tmp>i):
                s.discard(i)
                cnt+=1
        s.add(tmp)
        print(cnt)
    else:
        print(len(s))
