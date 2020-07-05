t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    areaList=[]
    areaList.append(max(arr))
    for i in range(n-1):
        for j in range(i+1,n):
            areaList.append((j-i+1)*min(arr[i:j+1]))
    maxArea=max(areaList)
    print(maxArea)