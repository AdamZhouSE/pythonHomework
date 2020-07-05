def getKeyValue(c):
    return arr.count(c)
num=int(input())

ans=[]
for i in range(num):
    n=int(input())
    arr = list(map(int, input().split()))
    arr=sorted(arr,key=lambda s:(getKeyValue(s),-s) ,reverse=True)
    ans.append(arr)
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j],end=" ")
        if j==len(ans[i])-1:
            print()
