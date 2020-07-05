n=int(input())
inp=input().split()
arr=[[] for i in range(n)]
for i in range(n):
    arr[i].append(int(inp[i]))
inp=input().split()
for i in range(n):
    arr[i].append(int(inp[i]))
for j in range(n):
    fang=0
    i=j
    road=[]
    while i<=n-1:
        fang+=arr[i][0]
        road.append(i)
        next=arr[i][1]
        if next-1 in road:
            print(fang)
            break
        else:
            i=next-1
            continue

