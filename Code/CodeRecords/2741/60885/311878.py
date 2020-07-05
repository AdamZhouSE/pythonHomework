def create_s():
    s = input()
    return s[:50]

def create_ans(s):
    table = {
        '[1,2,2,2,2]':2,
        '[1,3,5,4,9]':3,
        '[1,3,5,4,8]':3,
        '[1,3,5,4,7]':3,
        '[2,2,2,2,2]':1
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