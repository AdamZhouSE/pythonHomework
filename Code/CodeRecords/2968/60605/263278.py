def queryCircleSubs(s: str) -> int :
    s = list(s)
    leng = len(s)
    cnt = 0
    for i in range(0, leng):
        for j in range(i, leng):
            ss = list(s[i:j+1])
            os = ss.copy()
            os.reverse()
            if ss == os:
                cnt += 1

    return cnt

if __name__ == '__main__':
    s = input()
    q = int(input())
    ops = []
    for i in range(q):
        ops.append(input())

    for i in ops:
        if i[0] == "1":
            ins = i[2:]
            s = s + ins
        elif i[0] == "2":
            ins = i[2:]
            ins = list(ins)
            ins.reverse()
            s = "".join(ins) + s
        else:
            print(queryCircleSubs(s))