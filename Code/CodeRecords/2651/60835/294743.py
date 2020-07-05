for q in range(int(input())):
    n = int(input())
    string = ""
    while n > 0:
        string = string + str(n % 2)
        n = n // 2
    if len(string) % 2 == 1:
        string = string + "0"
    l = list(string)
    #l.reverse()
    for x in range(0, len(l), 2):
        tem = l[x]
        l[x] = l[x + 1]
        l[x + 1] = tem
    res = 0
    for x in range(len(l)):
        if l[x] == "1":
            res = res + 2**x
    print(res)