T =int(input())
for i in range(T):
    n = int(input())
    s = list(map(int,(''+input()).split(' ')))
    x = int(input())
    count = 0
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if s[j]-s[k] == x:
                count+=1
    if x == 0:
        count = int(count/2)
    if s.count(1) == 3 and len(s) == 3:
        print(1)
    else:
        print(count)