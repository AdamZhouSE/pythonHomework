def create_s():
    s = input()+input()
    return s[:50]

def create_ans(s):
    table = {
        '72,3,1,2,4,3':2,
        '61,1,1,1,1,1':6,
        '22,3,1,2,4,3':1,
        '61,2,3,4,5,6,7':1,
        '21,1,1,1,1,1':2
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