t=int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxlen,l,index = 0,0,0
    for i in range(1,n):
        if arr[i]==arr[i-1]+1:
            l += 1
            if l>maxlen:
                maxlen = l
        elif arr[i]==arr[i-1]:
            continue
        else:
            l = 0
    print(maxlen+1)