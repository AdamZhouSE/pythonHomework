nums=list(map(int,input().split(",")))
diff=int(input())
res={}
for i in nums:
    if i not in res:
        res[i]=""
    if i-diff in res:
        res[i-diff]=i
maxLength=1
for i in res:
    length=1
    next=res[i]
    while next!="":
        next=res[next]
        length=length+1
    maxLength=max(maxLength,length)
print(maxLength)