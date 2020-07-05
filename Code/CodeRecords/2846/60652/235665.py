n=int(input())
l=list(map(int,input().split(" ")))

step=0
l.remove(0)
if len(l)!=0:
    step=1
for i in range(0,len(l)-1):
    if l[i]!=l[i+1]:
        step+=1
print(step)        