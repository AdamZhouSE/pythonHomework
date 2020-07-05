count = int(input())
for n in range(count):
    info = input().split()
    a1=int(info[0])
    a2=int(info[1])
    tar=int(info[2])
    arr1=[int(x) for x in input().split()]
    arr2=[int(x) for x in input().split()]
    arr1.sort()
    pairs=[]
    for num in arr1:
        if tar-num in arr2:
            pairs.append((num,tar-num))
    l=len(pairs)
    if l == 0:
        print(-1)
    else:
        for i in range(l):
            print(pairs[i][0], end=' ')
            print(pairs[i][1])
    