t = int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    arr.sort()
    result=1
    temp=1
    for i in range(n-1):
        if arr[i]+1==arr[i+1]:
            temp+=1
            result=max(result,temp)
        elif arr[i]==arr[i+1]:pass
        else:
            temp=1
    print(result)