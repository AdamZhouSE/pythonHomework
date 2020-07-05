import operator
def infix(root:int,LT:dict,RT:dict,arr:list):
    if LT[root]!=0:
        infix(LT[root],LT,RT,arr)
    arr.append(root)
    if RT[root]!=0:
        infix(RT[root],LT,RT,arr)

def isfull(root:int,LT:dict,RT:dict,MaxDepth:int)->int:
    if LT[root]==0 and RT[root]==0:
        return MaxDepth
    elif LT[root]==0 and RT[root]!=0:
        return -1
    elif RT[root]==0 and LT[root]!=0:
        return -1
    else:
        Depth1=isfull(LT[root],LT,RT,MaxDepth+1)
        Depth2=isfull(RT[root],LT,RT,MaxDepth+1)
        if Depth1<Depth2 or Depth1-Depth2>1:
            return -1
        else: return Depth1

n,root=map(int,input().split())
LT={}
RT={}
z=[]
while len(LT)<n:
    fa,lch,rch=map(int,input().split())
    z.append((fa,lch,rch))
    LT[fa]=lch
    RT[fa]=rch
    if lch!=0:
        LT[lch]=0
        RT[lch]=0
    if rch!=0:
        LT[rch]=0
        RT[rch]=0
arr=[]
infix(root,LT,RT,arr)
x,y=operator.eq(arr,sorted(arr)),isfull(root,LT,RT,0)!=-1
if x and not y:
    x=False
print('true' if x else 'false')
print('true' if y else 'false')