def func(n:int):
    if n==0:
        return 2
    if n==1:
        return 1
    return func(n-1)+func(n-2)

tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(int(input()))
res=[]
for i in lists:
    print(func(i)%1000000007)