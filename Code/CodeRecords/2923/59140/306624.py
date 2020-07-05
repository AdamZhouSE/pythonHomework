temp=[int(x) for x in input().split(" ")]
n,q=temp[0],temp[1]
arr=[int(x) for x in input().split(" ")]
res=[0 for _ in range(n)]
for _ in range(q):
    temp = [int(x) for x in input().split(" ")]
    for i in range(temp[0]-1,temp[1]):res[i]+=1
res.sort()
arr.sort()
result=0
for i in range(n):
    result+=res[i]*arr[i]
print(result)
