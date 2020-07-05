T = int(input())
for i in range(T):
    ns = list(map(int, ('' + input()).split(' ')))
    n,s = ns[0],ns[1]
    a = ('' + input()).split(' ')
    a = list(map(int, a))
    temp = []
    for i in range(n):
        j = i
        while j < n:
            if sum(a[i:j+1]) == s:
                temp.append(i+1)
                temp.append(j+1)
                break
            j += 1
    if len(temp) == 0:
        print(-1)
    else:
        print(temp[0],end=' ')
        print(temp[1])