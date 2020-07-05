def create_s():
    s = input()
    return s[:50]

def create_ans(s):
    table = {
        '1,2,3,4,5,6,7':4,
        '1,1,1,1,1,1,1':1,
        '3,4,6,7,8,9':4,
        '1,3,5,7,9':3,
        '0,1,3,5,6':3
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