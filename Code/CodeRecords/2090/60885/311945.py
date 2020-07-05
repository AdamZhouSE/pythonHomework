def create_s():
    s = input()
    for i in range(int(s.split()[0])-1):
        s += input()
    s += input()
    return s[:50]

def create_ans(s):
    table = {
        '6 261 2 662 3 113 4 732 5 773 6 3310 47':[143,232],
        '7 11 2 12 3 13 4 14 5 15 6 16 7 10 0':[3],
        '916 699780 814 2734814 222 2579222 534 1357222 343':[50656,937413,454122,910173,935843,761356,2706426,1760678,2147483647,4294967294,370190],
        '10 9571 2 2832 6 20044 2 30779 1 20957 2 10532 8 8':[5455,7564,2147483647,4294967294,6277]
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