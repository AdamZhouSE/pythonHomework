T = int(input())
for i in range(0, T):
    string = input()
    template = input()
    temp = dict()
    for char in template:
        temp[char] = True
    ans = []
    for j in range(0, len(string) - len(template)):
        if string[j] not in temp:
            continue
        window = ""
        k = j
        for item in temp:
            temp[item] = True
        while True in temp.values() and k < len(string):
            if string[k] in temp:
                temp[string[k]] = False
            window += string[k]
            k += 1
        if True not in temp.values():
            ans.append(window)
    if not ans:
        print(-1)
    else:
        temp = [len(x) for x in ans]
        index = temp.index(min(temp))
        print(ans[index])
