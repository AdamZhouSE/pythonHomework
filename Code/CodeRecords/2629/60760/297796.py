def func(n:int):
    count=0
    res = ''

    while n>=1:
            res=res+str(n%2)
            n=int(n/2)
    return res.count('1')
tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))