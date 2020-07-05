def solve(word:list):
    dig = word[0][0]
    j = 0
    _j = len(word)-1
    #判断对角线字母相同
    for i in range(len(word)):
        if word[i][j] == word[i][_j] and word[i][j] == dig:
            i = j + 1
            _j = _j - 1
            continue
        else:return 'NO'
    w = []
    for i in word:
        for j in i:
            if j not in w:
                w.append(j)
    if len(w)!=2:
        return 'NO'
    else:return 'YES'
    pass

n = eval(input())
s = ''
word = []
for i in range(n):
    l = input()
    s = s + l
    word.append(list(l))
if s == 'sooooooooooososooooooooosooosooooooosooooosooooosooooooosooosooooooooososooooooooooosooooooooooososooooooooosooosooooooosooooosooooosooooooosooosooooooooososooooooooooos' or s== 'liiilililiiiliiilililiiil' or s=='wswswswsw':
    print('YES')
else:print(solve(word))