def func(n:int):
    res=0
    for i in range(1,n+1):
        res+=i**2
    return res
tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append( int(input()))
for i in lists:
    print(func(i))