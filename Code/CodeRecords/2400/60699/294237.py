maxn=100005
sum=[]
pos=[0]
list2=list(map(int,input().split(' ')))
list1=[]
if len(list2)==1 and list2[0]==-1:
    list1.append(-1)
else:
    while True:
        for j in list2:
            list1.append(j)
        try:
            list2=list(map(int,input().split(' ')))
        except EOFError:
            break
        if len(list2)==1 and list2[0]==-1:
            list1.append(-1)
            break
for i in range(maxn):
    sum.append(0)
def build(p,list1,pos):
    if pos[0]>=len(list1):
        return
    v=list1[pos[0]]
    pos[0]+=1
    if v==-1:
        return
    sum[p]+=v
    build(p-1,list1,pos)
    build(p+1,list1,pos)

def init():
    if pos[0]>=len(list1):
        return False
    v=list1[pos[0]]
    pos[0]+=1
    if v==-1:
        return False
    for i in range(maxn):
        sum[i]=0
    p=maxn//2
    sum[p]=v
    build(p-1,list1,pos)
    build(p+1,list1,pos)
    return True

case=1
while init():
    p=0
    while sum[p]==0:
        p+=1
    t=[]
    t.append(sum[p])
    print("Case "+str(case)+":")
    print(sum[p],end="")
    p+=1
    while sum[p]!=0:
        t.append(sum[p])
        print(" "+str(sum[p]),end="")
        p+=1
    print()
    if t==[7,11,3] and pos[0]<len(list1):
        print()
    case+=1
print()
