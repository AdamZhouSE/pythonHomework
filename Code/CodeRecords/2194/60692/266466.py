def count(num):
    res = []
    if num == 2:
        res.append('2')
    elif num < 2:
        res = []
    else:
        res.append("2")
        for m in range(3, num + 1, 2):
            flag = True
            for n in range(3, int(m ** 0.5) + 1):
                if m % n == 0 and m != n:
                    flag = False
                    break
            if flag:
                res.append(str(m))
    return res


num1 = int(input())
ans = []
for i in range(num1):
    n1_n2 = input().split(" ")
    n1 = int(n1_n2[0])
    n2 = int(n1_n2[1])
    l1 = count(n1)
    l2 = count(n2)
    if l1:
        for x in l1:
            if x in l2 and x != str(n1):
                l2.remove(x)
    ans.append(" ".join(l2))
for n in ans:
    print(n)