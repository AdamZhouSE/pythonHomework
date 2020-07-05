tests = int(input())
for i in range(0,tests):
    mark = []
    nums = int(input())
    ls = list(map(int,input().split(' ')))
    ls.sort()
    setn = list(set(ls))
    tem = [0]*len(setn)
    for j in range(0,len(tem)):
        tem[j] = ls.count(setn[j])
        for k in range(0,tem[j]):
            mark.append(str(setn[j]))
    print(' '.join(mark))