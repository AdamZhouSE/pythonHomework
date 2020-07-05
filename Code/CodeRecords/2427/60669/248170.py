t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    for item in arr:
        if arr.count(item)>1:
            print(arr.index(item)+1)
            break
        else:
            if arr.index(item)==len(arr)-1:
                print("-1")