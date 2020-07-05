def func(n:int):
    if n==1:
        return 1
    else:
        return n**2+func(n-1)
tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append( int(input()))
for i in lists:
    print(func(i))