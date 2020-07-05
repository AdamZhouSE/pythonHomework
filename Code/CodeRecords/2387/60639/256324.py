inp=input().split()
n=int(inp[0])
m=int(inp[1])
arr=list(map(int,input().split()))
sort=[]
for i in range(m):
    sort.append(list(map(int,input().split())))
q=int(input())
for i in range(m):
    l=sort[i][1]-1
    r=sort[i][2]
    if sort[i][0]==0:
        for j in range(r-l):
            for k in range(l,r-j-1):
                temp=0
                if arr[k+1]<arr[k]:
                    temp=arr[k]
                    arr[k]=arr[k+1]
                    arr[k+1]=temp
                else:
                    continue

    else:
        for j in range(r - l):
            for k in range(l, r - j-1):
                temp = 0
                if arr[k + 1] > arr[k]:
                    temp = arr[k]
                    arr[k] = arr[k + 1]
                    arr[k + 1] = temp
print(arr[q-1])
