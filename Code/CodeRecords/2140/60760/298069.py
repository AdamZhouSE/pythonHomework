def func(n:int):

    res=''
    times=n-1
    res=[n]
    while times>=1:
        res=[times]+res
        temp=times%len(res)
        res=res[len(res)-temp:]+res[0:len(res)-temp]
        times=times-1
    for i in range(len(res)):
        print(res[i], end=" ")
    print()
    return 0


tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    func(i)