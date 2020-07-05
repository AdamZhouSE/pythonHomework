n=""
get=""
while True:
    n=input()
    get+=n
    if n=="]":
        break
get=eval(get)
num=[]
for i in get:
    for j in i:
        if j!=0 and j>1:
            num.append(j)
num.sort()
rn=len(get)
cn=len(get[0])
tn=len(num)
out=[cn*rn]

def deep(cx,cy,temp,tindex,count):
    if get[cx][cy]==num[tindex]:
        temp[cx][cy]==1
        tindex+=1
    if tindex==tn:
        out.append(count)
        return
    if count>min(out):
        return
    if cx+1 in range(rn): 
        if get[cx+1][cy]!=0:
            deep(cx+1,cy,temp.copy(),tindex,count+1)
    if cx-1 in range(rn): 
        if get[cx-1][cy]!=0:
            deep(cx-1,cy,temp.copy(),tindex,count+1)
    if cy+1 in range(cn): 
        if get[cx][cy+1]!=0:
            deep(cx,cy+1,temp.copy(),tindex,count+1)
    if cy-1 in range(cn): 
        if get[cx][cy-1]!=0:
            deep(cx,cy-1,temp.copy(),tindex,count+1)

deep(0,0,get,0,0)
if min(out)==cn*rn:
    print(-1)
else:
    print(min(out))