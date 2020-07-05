t = int(input())
for _ in range(t):
    temp=[int(x) for x in input().split(" ")]
    n=temp[0]
    k=temp[1]
    arr=[int(x) for x in input().split(" ")]
    arr.sort()
    result=0
    for i in arr:
        if i<=k:
            k-=i
            result+=1
    print(result)