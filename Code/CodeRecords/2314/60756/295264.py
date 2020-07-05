def infix(root:int,LT:dict,RT:dict,arr:list):
    if LT[root]!=0:
        infix(LT[root],LT,RT,arr)
    arr.append(root)
    if RT[root]!=0:
        infix(RT[root],LT,RT,arr)

n=int(input())
LT={}
RT={}
fa,lch,rch=map(int,input().split())
root=fa
while len(LT)<n:
    LT[fa]=lch
    RT[fa]=rch
    if lch!=0:
        LT[lch]=0
        RT[lch]=0
    if rch!=0:
        LT[rch]=0
        RT[rch]=0
    fa, lch, rch = map(int, input().split())
arr=[]
infix(root,LT,RT,arr)
for i in arr:
    print("%d " %(i),end='')