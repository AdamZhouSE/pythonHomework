def f(i):
    if i == 1:
        return 1
    else:
        return f(i-1)+i-1
    
    
def recursive(i):
    if i == 1:
        return 1
    else:
        start = f(i)
        res = 1
        for k in range(i):
            res = res * start
            start = start + 1
        return recursive(i-1) + res


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    res = recursive(num)
    result.append(res)
for k in result:
    print(k)