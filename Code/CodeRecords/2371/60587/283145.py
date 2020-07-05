T = int(input())
while T > 0:
    T -= 1
    inp = input()
    tmp = ''
    for i in range(0, len(inp)):
        if inp[i].isalpha():
            tmp += inp[i]
    ntemp = tmp.upper()
    lst = list(ntemp)
    relst = list(ntemp)
    relst.reverse()
    isRe = True
    for i in range(0, len(lst)):
        if lst[i] != relst[i]:
            isRe = False
            break
    if isRe:
        print("YES")
    else:
        print("NO")
