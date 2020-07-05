n=int(input())
num=list(map(int,input().split()))
get=[]
count=0
for i in num:
    if i not in get:
        get.append(i)
        count+=1
if count==1 or count==3:
    print("YES")
else:
    print("NO")