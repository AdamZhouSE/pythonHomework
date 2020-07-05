n,c=map(int,input().split(" "))
list1=list(map(int,input().split(" ")))
if list1[0]<=c:
    count=1
else:
    count=0
for i in range(1,n):
    if list1[i]-list1[i-1]<=c:
        count+=1
    else:
        count=1
if c==0:
    print(0)
else:
    print(count)