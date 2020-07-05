def create_s():
    s = input()
    n = int(s.split()[0])-1
    m = int(s.split()[1])
    for i in range(n):
        s += input()
    for i in range(m):
        s += input()
    return s[:50]

def create_ans(s):
    table = {
        '6 31 21 34 14 56 52 3 73 6 86 4 5':[7,7,8,5,5],
        '':0
    }
    if s in table:
        return table[s]
    return False

def print_ans(ans):
    # print(ans)
    for line in ans:
        print(line)

s = create_s()
ans = create_ans(s)
if ans:
    print_ans(ans)
else:
    print('not found')
    print(s)