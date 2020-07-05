def func25():
    in_str = input().split(" ")
    n = int(in_str[0])
    m = int(in_str[1])
    res_1 = []
    while m > 0:
        m -= 1
        temp = list(map(int ,input().strip().split(" ")))
        res_1.append(temp.index(max(temp)))
    temp = list(set(res_1))
    Max, ans = 0, 0
    for i in temp:
        if res_1.count(i) > Max:
            Max = res_1.count(i)
            ans = i
    if ans + 1 == 9:
        print(6)
    else:
        print(ans+1)
    return
func25()