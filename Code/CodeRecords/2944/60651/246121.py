list1=list(input())
print(list1)
sum=0
for i in list1:
    if i =="(":
        sum+=1
    if i==")":
        sum-=1
    if sum<0:
        print("NO")
if sum==0:
    print("YES")
        