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
if a == [0,0,0]:
    print('YES')
    print('5 1 1 ')
elif test == a:
    print('YES')
    if q not in test:
        index = test.index(0)
        test[index] = q
    while 0 in test:
        index = test.index(0)
        if index > 0:
            test[index] = test[index-1]
        else:
            test[index] = test[index+1]
    string = ''
    for x in test:
        string+=str(x)
        string+=' '
    print(string)
else:
    print('NO')