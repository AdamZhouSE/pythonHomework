T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, ('' + input()).split(' ')))
    count = 0
    j = 0
    while j <= n-2:
        k = j+1
        while k <= n-1:
            if a[j] > a[k]:
                count+=1
            k+=1
        j+=1
    print(count)