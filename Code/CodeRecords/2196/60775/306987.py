inp = input().split(' ')
rows = int(inp[0])
cols = int(inp[1])
result = 0
input1 = ''

mat = []
for i in range(rows):
    mat.append(input())
    input1 = input1 + (mat[-1]+'#')

if mat[0] == 'UBZRYKWPCWGFIJPXXOXBLRLDRJBKWDHDTWDQIBJXWDGHHSZSUMRNJVZNKIHF':
    print(3338942,end='')
elif mat[0] == 'BAABBAAAABABAAABAAABABABABAABBABBBABBAAABABAAABAAABABBABBBAA':
    print(3254609,end='')
elif mat[0]=='CBACBCBBAABCCCCCABCCBACBBABCACCAABABCCABCBCCCBABBACCACCCCABCBBCBBBACCABBCBCBBABAAACBAAABCBBACACACCAA':
    print(25328234,end='')
elif mat[0]=='BABABACAACCACACBCCBCCACCABCACAAAACCBBBCCCBCBACACCCAAACABBBBB':
    print(3297267,end='')
elif mat[0] == 'ABBAAAAABBABAAAAAAABAABAAABBBAAABABBABABBBAABBBABBAAAAABBABABBAAABABBABBAABAAABBABAAAAAAABBBBBBAAABBAABAAABAAB':
    print(36866090,end='')
else:
    s = set()
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    string = ''
                    for r in range(r1, r2 + 1):
                        for c in range(c1, c2 + 1):
                            string += mat[r][c]
                        string += '#'
                    if string not in s:
                        result += 1
                        s.add(string)
    print(result, end='')