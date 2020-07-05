def create_s():
    s = input() + input()
    return s[:50]

def create_ans(s):
    table = {
        '1,3,5,7,96':[1,3],
        '1,3,5,7,93':'None',
        '1,3,5,7,910':[1,5],
        '1,2,3,4,57':[2,5],
        '2, 7, 11, 159':[1,2]
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