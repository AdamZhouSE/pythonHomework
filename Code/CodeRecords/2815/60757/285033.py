n=int(input())
li=list(map(int,input().split()))
step=0
for i in range(len(li)):
    if li[i]>0:
        step+=li[i]-1
    else:
        step+=abs(li[i]+1)
if(li.count(-1)%2==1):
    step+=2
print(step)