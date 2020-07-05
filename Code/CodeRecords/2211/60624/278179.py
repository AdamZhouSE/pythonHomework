def func10():
    temp = list(map(int, input().split(" ")))
    n = temp[0]
    k = temp[1]
    names = [input().split(" ")[0]]
    for i in range(n-1):
        names.append(input().split(" ")[0]+names[i])
    interesting_names = []
    while k > 0:
        k -= 1
        interesting_names.append(input())
    ans = []
    for interest in interesting_names:
        tmp = 0
        for name in names:
            if len(name) >= len(interest):
                if name[:len(interest)] == interest:
                    tmp += 1
        ans.append(tmp)
    for res in ans:
        print(res)
    return
func10()