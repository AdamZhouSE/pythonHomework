t = int(input())

while (t > 0):
    s = input()
    l = ["a", "e", "i", "u", "o", "A", "B", "I", "O", "U"]
    t1 = len(s)
    v = []
    for i in range(1, 2 ** t1):
        t2 = bin(i)
        t3 = len(t2)
        t4 = t2[2:t3]
        t12 = len(t4)
        t5 = "0" * (t1 - t12)
        t6 = t5 + t4
        s1 = str()
        for j in range(t1):
            if t6[j] == "1":
                s1 += s[j]
        v.append(s1)
    p = list(set(v))
    p.sort()
    flag = 0
    for i in p:
        if len(i) >= 2:

            if i[0] in l and i[-1] not in l:
                flag = 1
                print(i, end=" ")
    if flag == 0:
        print(-1, end=" ")
    print()
    t = t - 1
