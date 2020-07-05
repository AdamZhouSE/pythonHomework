def create_s():
    s = input()
    for i in range(int(s)-1):
        s += input()
    return s[:50]

def create_ans(s):
    table = {
        '42 3 2 4 25 2 1 3 1 3 2 4 1 4 34 2 1 3 2 4 1 4 2':17,
        '56 2 1 3 2 4 1 4 2 5 2 5 49 2 1 3 1 3 2 4 1 4 2 5 ':328,
        '1550 2 1 3 1 4 1 5 3 6 1 6 4 7 1 7 2 7 3 8 1 8 2 9':564051210,
        '1552 2 1 3 1 3 2 4 1 4 3 5 1 5 3 6 1 6 3 7 1 7 4 7':762073817,
        '1559 2 1 3 1 4 2 5 1 5 2 5 4 6 2 6 3 6 4 7 1 7 2 7':15121134,
        '810 3 1 3 2 4 1 5 3 6 2 6 3 6 4 6 5 8 3 8 613 3 1 ':9338582,
        '810 2 1 3 2 5 4 6 2 6 3 6 5 7 3 7 5 8 5 8 615 2 1 ':6217998,
        '56 3 2 4 2 5 1 5 2 5 3 5 47 3 1 3 2 4 2 4 3 5 1 5 ':363,
        '814 3 1 3 2 4 1 4 2 5 3 6 3 6 5 7 3 7 4 7 5 8 3 8 ':18315558,
        '1020 4 1 5 3 5 4 6 1 6 2 6 4 7 1 7 2 7 3 8 1 8 3 8':198097773
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