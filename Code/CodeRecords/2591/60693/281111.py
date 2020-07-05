def is_Prime(x:int):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

cases=int(input())
for _ in range(cases):
    n=int(input())
    if is_Prime(n+2):
        print('Yes')
    else:
        print('No')