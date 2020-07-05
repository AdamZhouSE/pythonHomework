testNum=int(input())
for i in range (testNum):
    rawInputs=input().split(' ')
    n=int(rawInputs[0])
    m=int(rawInputs[1])
    rawArr1=input().split(' ')
    rawArr2=input().split(' ')
    arr1=[]
    arr2=[]
    for rawArr1s in rawArr1:arr1.append(int(rawArr1s))
    for rawArr2s in rawArr2: arr2.append(int(rawArr2s))
    ans=arr1+arr2
    ans.sort()
    print(' '.join(str(i)for i in ans),'')