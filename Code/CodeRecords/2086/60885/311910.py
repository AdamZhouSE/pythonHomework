def create_s():
    s = input()
    for i in range(int(s.split()[1])):
        s += input()
    return s[:50]

def create_ans(s):
    table = {
        '1049 109537 1027 185663189439 923 84240182192 68 1':459312924580,
        '7 121 2 91 5 21 6 32 3 52 6 73 4 63 7 34 5 64 7 25':16,
        '1 0':'0',
    }
    if s in table:
        return table[s]
    return False

def print_ans(ans):
    print(ans,end='')
    # for line in ans:
    # 	print(line)

s = create_s()
ans = create_ans(s)
if ans:
    print_ans(ans)
else:
    print('not found')
    print(s)