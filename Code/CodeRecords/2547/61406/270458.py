T = int(input())
for x in range(0,T):
    n = int(input())
    array = input().split()
    k = int(input())
    result = []
    for i in range(0,n):
        for j in range(0,i):
            result.append((array[i],array[j]))
        for j in range(i+1,len(array)):
            result.append((array[i],array[j]))
    count = 0
    y = 0
    while y<len(result):
        if result.count(result[y])==1:
            if int(result[y][0])-int(result[y][1])==k:
                count = count+1
        elif result.count(result[y])!=1:
            result.remove(result[y])
            y = y-1
        y = y+1
    print(count)

