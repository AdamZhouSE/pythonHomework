for q in range(int(input())):
    def to_binary(n):
        string = ""
        while n > 0:
            string = string + str(n % 2)
            n = n // 2
        return string
    def to_int(bin_res):
        res = 0
        for x in range(len(bin_res)):
            res = res + int(bin_res[x])*(2**x)
        return res
    n = int(input())
    bin_n = to_binary(n)
    res = []
    for x in range(n + 1):
        bin_x = to_binary(x)
        bin_res = ""
        for y in range(min(len(bin_n), len(bin_x))):
            if bin_n[y] == bin_x[y] and bin_n[y] == "1":
                bin_res = bin_res + "1"
            else:
                bin_res = bin_res + "0"
        #print(bin_res, x)
        m = to_int(bin_res)
        if m not in res:
            res.append(m)
    res.sort(reverse = True)
    for x in res:
        print(x,end = " ")
    print()