n=int(input())
arr = [int(x) for x in input().split(" ")]
res=[]
maxNum=0
for i in arr:
    if res.count(i)==0:res.append(i)
    else:res.remove(i)
    maxNum=max(maxNum,len(res))
print(maxNum)