def seq(n):
    lst = []
    for i in range(n):
        lst.append(i)
    out_seq = []
    count = 1
    while count <= n:
        for i in range(count):
            lst.append(lst[0])
            del lst[0]
        out_seq.append(lst[0])
        del lst[0]
        count += 1
    res = []
    for i in range(n):
        res.append(0)
    for i in range(n):
        res[out_seq[i]] = i+1
    return res

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(seq(n))
    for res in ans:
        print(*res)