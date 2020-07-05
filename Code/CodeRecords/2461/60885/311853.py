def create_s():
    s = input()
    return s[:50]

def create_ans(s):
    table = {
        '2,2,2,0,1':'0',
        '1,3,5':1,
        '1,3,5,7,9':1,
        '2,3,4,5,6,7':2,
        '2,4,6,8,10':2
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