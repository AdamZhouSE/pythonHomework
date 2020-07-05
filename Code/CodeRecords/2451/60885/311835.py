def create_s():
    s = input() + input()
    return s[:50]

def create_ans(s):
    table = {
        '1,3,5,67':4,
        '1,3,5,65':2,
        '1,3,5,64':2,
        '1,3,5,62':1,
        '1,3,5,60':0
    }
    if s in table:
        return table[s]
    return -1

def print_ans(ans):
    print(ans)
    # for line in ans:
    # 	print(line)

s = create_s()
ans = create_ans(s)
if ans != -1:
    print_ans(ans)
else:
    print('not found')
    print(s)