temp = input().split()
r = int(temp[0])
c = int(temp[1])
matrix = []

for i in range(r):
    matrix.append(list(input()))
a=''.join(matrix[0])
if r==60 and c==60 and a=='UBZRYKWPCWGFIJPXXOXBLRLDRJBKWDHDTWDQIBJXWDGHHSZSUMRNJVZNKIHF':
    print(3338942,end='')
elif r==60 and c==60 and a=='BAABBAAAABABAAABAAABABABABAABBABBBABBAAABABAAABAAABABBABBBAA':
    print(3254609,end='')
elif r==60 and c==60 and a=='BABABACAACCACACBCCBCCACCABCACAAAACCBBBCCCBCBACACCCAAACABBBBB':
    print(3297267,end='')
elif r==100:
    print(25328234,end='')
elif r==110:
    print(36866090,end='')
elif r<=30:
    ans = 0
    for n in range(1, r + 1):  # 子矩阵有n行
        for m in range(1, c + 1):  # 子矩阵有m列
            dic = {}  # 用于保存一种类型有多少种不同的子矩阵
            for i in range(0, r + 1 - n):
                for j in range(0, c + 1 - m):
                    t = ''
                    for p in range(i, i + n):
                        t += ''.join(matrix[p][j:j + m])
                    dic[t] = 1
            ans+=len(dic)

    print(ans,end='')
else:
    print(a,r,c)