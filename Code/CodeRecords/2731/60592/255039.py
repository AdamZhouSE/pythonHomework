tests = int(input())
for i in range(0,tests):
    nums = int(input())
    ls = list(map(int,(input().split(' '))))
    setn = list(set(ls))
    res = 0
    for j in range(0,len(setn)):
        tem = ls.count(setn[j])
        res+=int(tem/2)*2
    print(res)