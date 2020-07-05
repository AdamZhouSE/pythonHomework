def func(n:int):
    return n^^3

tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))