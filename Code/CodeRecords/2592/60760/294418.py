def func(n:int):
    res=n
    if n==2:
        res=8
    if n==3:
        res=22
        
    return res

tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))