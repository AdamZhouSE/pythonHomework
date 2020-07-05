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
        Depth=isfull(LT[root],LT,RT,MaxDepth+1)
        return -1 if isfull(RT[root],LT,RT,MaxDepth+1)>Depth else Depth

n,root=map(int,input().split())
LT={}
RT={}
while len(LT)<n:
    fa,lch,rch=map(int,input().split())
    LT[fa]=lch
    RT[fa]=rch
    LT[lch]=0
    RT[lch]=0
    LT[rch]=0
    RT[rch]=0
arr=[]
infix(root,LT,RT,arr)
print('true' if operator.eq(arr,sorted(arr)) else 'false')
print('true' if isfull(root,LT,RT,0)!=-1 else 'false')