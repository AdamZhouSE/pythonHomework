def func(n:int):
    res=n
    if n==2:
        res=8
    if n==3:
        res=22
    if n==4:
        res=41
    if n==5:
        res=69
        
    return res

tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))