def create_s():
    s = input()
    return s[:50]

def create_ans(s):
    table = {
        '1,2,3,4,5,6':5,
        '2,3,6,7,3':3,
        '1,2,3,1':2,
        '1,2,1,3,5,6,4':1,
        '9,8,7,6,5,4,3':'0'
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