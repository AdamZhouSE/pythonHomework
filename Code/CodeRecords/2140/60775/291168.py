T = int(input())
for t in range(T):
    n = int(input())
    result = []
    while n > 0:
        result.insert(0,n)
        #回滚n次
        for i in range(n):
            l = len(result)
            result = result[l-1:l] + result[:l-1]
        n -= 1
    print(' '.join(str(x) for x in result))