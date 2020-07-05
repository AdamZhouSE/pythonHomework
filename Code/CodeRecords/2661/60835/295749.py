def to_binary(n):
    string = ""
    while n > 0:
        string = string + str(n % 2)
        n = n // 2
    #string = string[::-1]
    return string
for q in range(int(input())):
    n = to_binary(int(input()))
    cnt_0 = 0
    cnt_1 = 0
    for x in range(len(n)):
        if n[x] == "0":
            cnt_0 = cnt_0 + 1
        else:
            cnt_1 = cnt_1 + 1
    #print(cnt_0,cnt_1)
    bin_0 = to_binary(cnt_0)
    bin_1 = to_binary(cnt_1)
    if len(bin_0) > len(bin_1):
        for x in range(len(bin_0) - len(bin_1)):
            bin_1 = bin_1 + "0"
    else:
        for x in range(len(bin_1) - len(bin_0)):
            bin_0 = bin_0 + "0"
    bin_res = ""
    for x in range(len(bin_0)):
        if bin_0[x] != bin_1[x]:
            bin_res = bin_res + "1"
        else:
            bin_res = bin_res + "0"
    #print(bin_res)
    res = 0
    for x in range(len(bin_res)):
        res = res + int(bin_res[x])*(2**x)
    print(res)
            