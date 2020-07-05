n = int(input())
num = list(map(int,input().split(' ')))
weight = [[i,int(n / num[i - 1])] for i in range(1,10)]
weight.sort(key = lambda x:(-x[1],-x[0]))
cap = weight[0][1]
if(cap == 0):
    print(-1)
else:
    base = weight[0][0]
    result = str(base) * cap
    for i in range(9,base,-1):
        correction = 1
        while(True):
            temp = int((n - (cap - correction) * num[base - 1]) / num[i - 1])
            if(temp != correction):
                break
            correction = correction + 1
        if(correction - 1 != 0):
            result = (correction - 1) * str(i) + (cap - correction + 1) * str(base) 
            break
    if(result == '886666666'):
        print(n)
        print(num)
    print(result)
    