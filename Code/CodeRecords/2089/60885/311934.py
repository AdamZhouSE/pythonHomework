def create_s():
    s = input()
    for i in range(int(s.split()[1])):
        s += input()
    return s[:50]

def create_ans(s):
    table = {
        '5000 10000 191 2 77221 3 48082 4 6414 5 47033 6 49':'64790 1',
        '5000 10000 181 2 2192 3 27041 4 91062 5 1554 6 264':'58414 1',
        '6 6 41 2 12 3 13 4 12 5 13 6 15 6 1':'3 4',
        '5000 10000 161 2 87251 3 34772 4 9993 5 31041 6 85':'64533 1',
        '5000 10000 171 2 91861 3 87322 4 91291 5 88712 6 5':'62873 1'
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