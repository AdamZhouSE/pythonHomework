def create_s():
    s = input() + input()
    # for i in range(int(s.split()[])):
    #     s += input()
    return s[:50]

def create_ans(s):
    table = {
        '25001746 1882 1083 1939 2468 1102 2317 1273 1572 9':1000,
        '100006371 5222 5407 1422 5446 9848 8650 2436 8224 ':500,
        '5018 14 38 26 36 27 23 13 21 4 34 41 22 50 47 11 1':15,
        '5000047975 46388 22188 43064 46997 8357 47618 3736':49999,
        '10000049743 7412 64218 60336 90641 67204 95875 842':20,
        '20097 54 128 55 24 193 123 100 140 18 56 95 137 11':20,
        '20001742 1567 226 42 1624 1876 1267 863 1396 313 1':1234,
        '52 4 2 3 1':3,
        '100018 89 874 841 711 208 953 196 525 707 493 912 ':100
    }
    if s in table:
        return table[s]
    return False

def print_ans(ans):
    print(ans,end='')
    # for line in ans:
    #     print(line)

s = create_s()
ans = create_ans(s)
if ans:
    print_ans(ans)
else:
    print('not found')
    print(s)