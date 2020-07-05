tests = int(input())
for i in range(0,tests):
    mark = []
    nums = int(input())
    ls = list(map(int,input().split(' ')))
    setn = list(set(ls))
    setn.sort()
    tem = [0]*len(setn)
    for j in range(0,len(tem)):
        tem[j] = ls.count(setn[j])
    index = -1
    for k in range(0,len(setn)):
        max = 0
        for h in range(0,len(setn)):
            if max<tem[h]:
                max = tem[h]
                index = h
        tem[index] = 0
        for h in range(0,max):
            mark.append(str(setn[index]))
    if i == tests-1:
        print(' '.join(mark),end=' ')
        print()
    else:
        print(' '.join(mark),end=' ')
        print()