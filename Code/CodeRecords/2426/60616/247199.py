testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawArr=input().split(' ')
    arr=[]
    for item in rawArr:arr.append(int(item))
    ans=[]
    arr.sort()
    for j in range(0,size-2):
        for n in range(j+1,size-1):
            for m in range(n+1,size):
                tmp=arr[j]*arr[n]*arr[m]
                ans.append(tmp)
    print(max(ans))