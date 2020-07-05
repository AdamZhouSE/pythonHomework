def func26():
    n = int(input())
    s = []
    flag = False
    while n > 0:
        n -= 1
        s.append(int(input()))
    Sum = sum(s)
    if Sum % 360 == 0:
        print("YES")
    else:
        if Sum % 2 != 0:
            print("NO")
        else:
            bit = 1 << len(s)
            for i in range(1,bit):
                the_sum = 0
                for j in range(len(s)):
                    if (i & 1 << j) != 0:
                        the_sum += s[j]
                if the_sum * 2 == Sum:
                    flag = True
                    print("YES")
                    break
            if not flag:
                print("NO")
    return
func26()