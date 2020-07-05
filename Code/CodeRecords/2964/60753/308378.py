import sys
tempans=0
a=""
b=""
lena=0
lenb=0
ans=[0]*10
def dfs(dx,dy,dep,a,b,lena,lenb,tempans):
    if dep+abs((lena-dx)-(lenb-dy))>=tempans:
        return
    while   dx<lena and dy<lenb:
        if a[dx]==b[dy]:
            dx+=1
            dy+=1
        else:
            break
    if dx==lena:
        tempans=min(tempans,dep+lenb-dy)
        return
    if dy==lenb:
        tempans=min(tempans,dep+lena-dx)
        return
    dfs(dx+1,dy+1,dep+1,a,b,lena,lenb,tempans)
    dfs(dx+1,dy,dep+1,a,b,lena,lenb,tempans)
    dfs(dx,dy+1,dep+1,a,b,lena,lenb,tempans)
n=int(input())
s=sys.stdin.read()
slist=s.split("\n")
slist.sort(key= lambda x:len(x),reverse=False)
for i in range(n):
    a=slist[i]
    lena=len(a)
    for j in range(i+1,n):
        if abs(len(slist[j])-len(slist[i]))<9:
            b=slist[j]
            lenb=len(b)
            tempans=9
            dfs(0,0,0,a,b,lena,lenb,tempans)
            ans[tempans]+=1
out=""
for i in range(1,9):
    out+=str(ans[i])+" "
sys.stdout.write(out)
               
               
               
               
    