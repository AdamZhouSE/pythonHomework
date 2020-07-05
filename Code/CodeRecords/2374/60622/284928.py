def getKeyValue(c):
    return arr.count(c)
num=int(input())

ans=[]
for i in range(num):
    n=int(input())
    arr = list(map(int, input().split()))
    arr=sorted(arr,key=getKeyValue,reverse=True)
    ans.append(arr)
for n in ans:
    print(" ".join(str(i) for i in n))