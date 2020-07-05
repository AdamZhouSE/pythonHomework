
def solve():
    num = int(input())
    i = 2
    str_n = list(str(num))
    if str_n[0] == '1':
        str_n = str_n[1:]
        str_n.sort(reverse= True)
        if str_n[0] == 0:
            print(num - 1)
            return 
    while True:
        k = 0
        tmp = num
        tmp = tmp - i ** k
        while tmp >= 0:
            if tmp == 0:
                print(i)
                return
            else:
                k += 1
                tmp = tmp - i ** k
        i += 1

solve()