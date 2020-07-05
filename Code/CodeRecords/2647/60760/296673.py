def func(n: int):
    i=0
    while (pow(2,i)+1)-1<=n:
        if (pow(2,i)+1)-1==n:
            return 1
        i+=1
    return 2


tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))