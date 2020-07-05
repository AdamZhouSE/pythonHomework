apples=int(input())
people=int(input())
ans=[0]*people
index=0
while(apples!=0):
    if apples-(index+1)>=0:
        ans[index%people]+=index+1
        apples-=index+1
        index+=1
    else:
        ans[index%people]+=apples
        apples=0
print(ans)