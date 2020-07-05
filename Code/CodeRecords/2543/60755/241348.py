NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    eg = input().split(" ")
    res = []
    for m in range(1, num + 1):
        all_max = 0
        for k in range(num - m + 1):
            min = 100000
            temp = eg[k:k+m]
            for n in temp:
                if int(n) < min:
                    min = int(n)
            if min > all_max:
                all_max = min
        res.append(str(all_max))
    res.sort(reverse=True)
    result.append(" ".join(res))
for i in result:
    print(i)
