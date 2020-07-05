T=int(input())
for t in range(T):
    N=int(input())
    if N==1:
        print(1)
        continue
    arr=[N-1,N]
    count=N-1
    while len(arr)<N:
        for i in range(count):
            arr.insert(0,arr.pop(-1))
        arr.insert(0,count-1)
        count-=1
    arr.insert(0,arr.pop(-1))
    print(' '.join(map(str,arr)))