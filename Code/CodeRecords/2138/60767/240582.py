def getSum(windowSize,arr,res):
    for i in range(0,len(arr)-windowSize+1):
        sum = 0
        for x in range(0,windowSize):
            sum = sum + arr[i+x]
        res.append(sum)

inp = input().split(",")
arr = []
for i in inp:
    arr.append(int(i))
k = int(input())
res = []
for i in range(2,len(arr)+1):
    getSum(i,arr,res)
flag = 0
for x in res:
    if(x%k==0):
        flag = 1
        break
if(flag==1):
    print(True)
else:
    print(False)