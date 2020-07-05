def func(n: int):
    if n==1:
        return 1
    if n==2:
        return 1
    i=0
    while (pow(2,i)-1)<=n:
        i+=1
    return 1+func(n+1-pow(2,i-1))


tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))