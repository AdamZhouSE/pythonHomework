testNum=int(input())
for i in range (testNum):
    rawInputs=input().split(' ')
    size=int(rawInputs[0])
    num=int(rawInputs[1])
    rawArr=input().split(' ')
    arr=[]
    for item in rawArr:arr.append(int(item))
    arr.sort()
    ans=[]
    for j in range (num):
        ans.append(arr[size-1-j])
    print(' '.join(str(m)for m in ans),'')