def func(n:int):
    count=0
    res = ''
    for i in range(1,n+1):
        
        while i>=1:
            res=res+str(i%2)
            i=int(i/2)
    return res.count('1')
tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))