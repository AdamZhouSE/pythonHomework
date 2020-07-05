def func(n:int):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+i
    if sum<2*n:
        return 1
    else:
        return 0
tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))