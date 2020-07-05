All = int(input())

for q in range(0, All):
    temp = input().split()
    n=int(temp[0])
    p=int(temp[1])
    ar = list(map(int, input().split()))

    ans="No"
    for i in range(n-1):
        for j in range(i+1,n):
            if ar[i]*ar[j]==p:
                ans="Yes"
                break
    print(ans)