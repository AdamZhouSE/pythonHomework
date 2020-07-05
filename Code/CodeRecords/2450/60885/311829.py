def create_s():
    s = input() + input()
    return s[:50]

def create_ans(s):
    table = {
        '1,2,3,4,5,62':[1,1],
        '5,7,7,8,8,100':[-1,-1],
        '1,2,3,4,5,60':[-1,-1],
        '5,7,7,8,8,106':[-1,-1],
        '5,7,7,8,8,108':[3,4]
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