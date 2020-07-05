list1=list(input())
sum=0
for i in list1:
    if i =="(":
        sum+=1
    if i==")":
        sum-=1
    if sum<0:
        print("NO",end="")
if sum==0:
    print("YES",end="")
else:
    print("NO",end="")
        