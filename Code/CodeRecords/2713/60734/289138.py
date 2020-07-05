n, q = input().split()
n, q = int(n), int(q)
a = list(map(int, input().split()))

test = [0 for i in range(n)]
for i in range(1, q+1):
    if i in a:
        begin = a.index(i)
        end = len(a) - a[::-1].index(i)
        for j in range(begin, end):
            test[j] = i
if test == a:
    print('YES')
    while 0 in test:
        index = test.index(0)
        if index > 0:
            test[index] = test[index-1]
        else:
            test[index] = test[index+1]
    for x in test:
        print(x,end = ' ')
else:
    print('NO')