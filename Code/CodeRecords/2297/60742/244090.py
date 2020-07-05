try:
    n = int(input())
    a = input().split()
    d = int(input())
    num = 1
    count = 0
    for i in range(d-1):
        count += num
        num *= 2
    if count>n:
        print("EMPTY")
    else:
        res = []
        max_index = min(count+num,n)
        for i in range(count,max_index):
            res.append(a[i])
        print(' '.join(res))
except EOFError:
    pass