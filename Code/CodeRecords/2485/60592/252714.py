tests = int(input())
for i in range(0,tests):
    num = int(input())
    ls = input().split(' ')
    res = []
    for j in range(0,num):
        stri = list(ls[j])
        stri.sort()
        res.append(''.join(stri))
    setn = list(set(res))
    lent = []
    for h in range(0,len(setn)):
        lent.append(str(res.count(setn[h])))
    lent.sort()
    print(' '.join(lent))