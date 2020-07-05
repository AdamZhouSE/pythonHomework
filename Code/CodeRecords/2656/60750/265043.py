

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        line = list(map(int,input().split(' ')))
        m = line[0]
        n = line[1]
        count = 1
        if m == n:
            res.append(-1)
        else:
            bin_m = "{0:b}".format(m)
            bin_n = "{0:b}".format(n)
            if len(bin_m) > len(bin_n):
                tmp = ['0' for i in range(len(bin_m) - len(bin_n))]
                tmp = "".join(tmp)
                bin_n = tmp + bin_n
            elif len(bin_n) > len(bin_m):
                tmp = [0 for i in range(len(bin_m) - len(bin_n))]
                tmp = "".join(tmp)
                bin_m = tmp + bin_m

            j = len(bin_m) - 1
            while bin_m[j] == bin_n[j]:
                count += 1
                if j == 0:
                    res.append(-1)
                    break
                else:
                    j = j - 1
            if bin_m[j] != bin_n[j]:
                res.append(count)

    for i in range(0,test):
        print(res[i])

solve()

