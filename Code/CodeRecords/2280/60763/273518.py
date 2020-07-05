T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, ('' + input()).split(' ')))
    a.sort()
    i = 1
    while i < n:
        if i != a[i-1]:
            print(i)
            break
        i +=1