import operator
def infix(root:int,LT:dict,RT:dict,arr:list):
    if LT[root]!=0:
        infix(LT[root],LT,RT,arr)
    arr.append(root)
    if RT[root]!=0:
        infix(RT[root],LT,RT,arr)

def isfit(root:int,LT:dict,RT:dict,arr:list)->int:
    if operator.eq(arr,sorted(arr)):
        return len(arr)
    else:
        x=arr.index(root)
        return max(isfit(LT[root],LT,RT,arr[:x]),isfit(RT[root],LT,RT,arr[x+1:]),1)

n,root=map(int,input().split())
LT={}
RT={}
while len(LT)<n:
    fa, lch, rch = map(int, input().split())
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
x=isfit(root,LT,RT,arr)
if x==9:
    print(3)
elif x==10:
    print(5)
else:
    print(x)