while True:
    n = int(input())
    if n == 0:
        break
    strings = []
    for i in range(n):
        strings.append(input())
    string = input()
    count = {}.fromkeys(strings)
    for x in strings:
        cnt = 0
        begin = 0
        while x in string[begin:]:
            cnt += 1
            begin = string.index(x, begin)+1
        count[x] = cnt
    max_cnt = max(count.values())
    print(max_cnt)
    for k,v in count.items():
        if max_cnt == v:
            print(k)