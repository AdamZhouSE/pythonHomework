

def solve():
    n = int(input())
    i = 1
    tmp = ''
    while True:
        tmp += str(i)
        if len(tmp) >= n:
            print(tmp[n- 1])
            return
        else:
            i += 1

solve()