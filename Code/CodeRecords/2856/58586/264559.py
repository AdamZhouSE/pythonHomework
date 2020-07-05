trees=int(input())
arr=[]
for i in range(trees):
    arr.append(list(map(int,input().split(" "))))
if trees==1:
    print(1)
else:
    count=2
    for i in range(1, trees - 1):
        left=arr[i][0]-arr[i-1][0]
        right=arr[i+1][0]-arr[i][0]
        if left>arr[i][1]:
            count+=1
            continue
        elif right>arr[i][1]:
            count+=1
            arr[i][0]+=arr[i][1]
    print(count)