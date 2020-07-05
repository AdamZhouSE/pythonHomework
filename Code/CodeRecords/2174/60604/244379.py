a=input().split()
island=int(a[0])
n=int(a[1])
isl=[i for i in range(1,island+1)]
print(isl)
class bridge:
    side1=0
    side2=0
    dange=0
    exist=False
    def build(self,d):
        self.dange=d
        self.exist=True
    def __init__(self,is1,is2):    
        self.side1=is1
        self.side2=is2
        self.dange=0
        self.exist=False
    
    def destroy(self):
        self.dange=0
        self.exist=False
print(pailie("12"))
tmp=[]

def findway(isl,is1,is2,bridge):
    if is1>is2:
        is1=tmp
        tmp=is2
        is2=is1
    res=[]
    for i in brigde:
        if i.side1==is1:
            is1=i.side2
            findw

for i in range(len(isl)-1):
    for j in range(i+1,len(isl)-1):
        tmp.append(bridge(i,j))
for i in range(n):
    now=input().split()
    for i in range(len(now)):
        now[i]=int(now[i])
    if now[0]==0:
        #print(now)
        for i in tmp:
            if (i.side1==now[1] and i.side2==now[2]) or(i.side1==now[2] and i.side2==now[1]):
                i.build(now[3])
                break
                print(i.dange)
    elif now[0]==1:
        print(now)
        for i in tmp:
            if (i.side1==now[1] and i.side2==now[2]) or(i.side1==now[2] and i.side2==now[1]):
                i.destroy()
    elif now[0]==2:
        print(now)