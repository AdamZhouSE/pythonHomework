t = int(input())
for i in range(t):
    n= int(input())
    arr = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                ans+=1
    print(ans)  