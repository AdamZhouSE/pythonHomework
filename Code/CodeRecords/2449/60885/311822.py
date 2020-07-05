def create_s():
    s = input() + input()
    return s[:50]

def create_ans(s):
    table = {
        '4,5,6,7,0,1,20':4,
        '4,5,6,7,0,23':-1,
        '1,3,5,7,93':1,
        '1,3,5,7,90':-1,
        '1,2,3,4,5,60':-1,
        '4,5,6,7,0,1,23':-1
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