def func(n:int):
    return (int(pow(3,0.5)/2*n)*4-n)*n

tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))