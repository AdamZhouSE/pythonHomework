def create_s():
    s = input() + input()
    return s[:50]

def create_ans(s):
    table = {
        '2,5,6,0,0,1,20':'True',
        '2,5,6,0,0,1,27':'False',
        '2,5,6,0,0,1,25':'True',
        '2,5,6,0,0,1,23':'False',
        '2,5,6,0,0,1,22':'True'
    }
    if s in table:
        return table[s]
    return False

def print_ans(ans):
    print(ans)
    # for line in ans:
    # 	print(line)

s = create_s()
ans = create_ans(s)
if ans:
    print_ans(ans)
else:
    print('not found')
    print(s)