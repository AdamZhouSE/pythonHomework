n = int(input())
num = list(map(int,input().split(' ')))
weight = [[i,n / num[i - 1]] for i in range(1,10)]
weight.sort(key = lambda x:(-x[1],-x[0]))
cap = int(weight[0][1])
if(cap == 0):
    print(-1)
else:
    base = weight[0][0]
    result = str(base) * cap
    w = num[base - 1] * cap
    for i in range(9,base,-1):
        correction = 1
        while(w + correction * (num[i - 1] - num[base - 1]) <= n):
            correction = correction + 1
        if(correction - 1 != 0):
            result = (correction - 1) * str(i) + result[:-(correction - 1)]
            w = correction * (num[i - 1] - num[base - 1]) + w
    print(result)
    