def ishui(x):
    strr=str(x)
    i=0
    j=len(strr)-1
    while i<j:
        if strr[i]!=strr[j]:
            return False
        i+=1
        j-=1
    return True

l=int(input())
r=int(input())
hui=[]
for i in range(l,r+1):
    if ishui(i):
        hui.append(i)
cnt=0
for i in range(0,len(hui)):
    tmp=hui[i]*hui[i]
    if tmp>r:
        break
    if tmp in hui:
        cnt+=1
print(cnt)