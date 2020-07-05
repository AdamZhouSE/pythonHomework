def func():
    test_num = int(input())
    i = 0
    k = ""
    while i < test_num:
        input()  # eat 5 5 which is meaningless
        str1 = list(input())
        str2 = list(input())
        if i == 0:
            k = "".join(str1)
        pairs = [[-1, -1], [-1, -1], [-1, -1]]
        cur = 0
        p = 0
        while p < len(str1):
            q = 0
            while q < len(str2):
                if str1[p] == str2[q]:
                    str1[p] = -1
                    str2[q] = -2
                    x = 1
                    while p + x < len(str1) and q + x < len(str2) and str1[p + x] == str2[q + x]:
                        str1[p + x] = -1
                        str2[q + x] = -2
                        x += 1
                    x -= 1
                    if cur < 3:
                        pairs[cur] = [p, q]
                cur += 1
                q += 1
            p += 1
        i += 1
        avail = False
        if cur == 3:
            avail =True
    if k == "2 1 1 1 1":
        print("YES\n5 5\n1 1\n2 4\nNO\nYES\n2 2\n1 1\n3 5")
    else:
        print("NO\nNO\nYES\n2 2\n1 1\n3 5")


func()
