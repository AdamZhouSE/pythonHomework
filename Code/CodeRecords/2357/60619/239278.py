t = int(input())
for index in range(t):
    l = input().split(" ")
    len1 = int(l[0])
    len2 = int(l[1])
    target = int(l[2])
    arr1 = input().split()
    arr2 = input().split()
    pairs = []
    for i in arr1:
        for j in arr2:
            if int(i)+int(j) == target:
                pair = []
                pair.append(i)
                pair.append(j)
                pairs.append(pair)
    if len(pairs) == 0:
        print(-1)
    else:
        for i in pairs:
            print(*i)
