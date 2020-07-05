def func(arr:list):
    res=[]
    for i in arr:
        if i%2==0:
            res.append(i)
    for i in arr:
        if i%2==1:
            res.append(i)
    for i in range(len(res)):
        print(res[i],end=" ")
    print()
    return 0
tests = int(input())  # 找规律
lists = []
for i in range(tests):
    a = input()
    lists.append(list(map(int, input().split(' '))))
for i in lists:
    (func(i))