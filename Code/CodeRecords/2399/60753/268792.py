import sys
import re
def fullarrange(n):
    if n==0:
        return 1
    ans=1
    while n>=1:
        ans*=n
        n-=1
    return ans
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
t = nums[0]
del (nums[0])
for i in range(t):
    n = nums[0]
    del (nums[0])
    m = nums[0]
    del (nums[0])
    l = nums[0]
    del (nums[0])
    r = nums[0]
    del (nums[0])
    numlist = nums[:n]
    del (nums[:n])
    total = fullarrange(n+m)
    subtotal = 1
    numlist.sort()
    filters = list(set(numlist))
    filters.sort()
    s = len(filters)
    count = [0] * s
    for j in range(n):
        indx = filters.index(numlist[j])
        count[indx] += 1
    span = r -l+ 1
    countsp = [0] * span
    for h in range(r-l + 1):
        if l + h not in filters:
            m -= 1
            countsp[h] += 1
    while m > 0:
        refrepete = 0
        reforigin = 0
        addorigin = 100000
        addrepete = 100000
        for h in range(r-l + 1):
            if l + h in filters:
                indexer = filters.index(l + h)
                if count[indexer] + 1 < addorigin:
                    addorigin = count[indexer] + 1
                    reforigin = indexer
            else:
                if countsp[h] + 1 < addrepete:
                    addrepete = countsp[h] + 1
                    refrepete = h
        if addorigin <= addrepete:
            count[reforigin] += 1
        else:
            countsp[refrepete] += 1
        m -= 1
    for w in range(len(filters)):
        subtotal *= fullarrange(count[w])
    for h in range(r-l + 1):
        if l + h not in filters:
            subtotal *= fullarrange(countsp[h])
    print(total // subtotal)


