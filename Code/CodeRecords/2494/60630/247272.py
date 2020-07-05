num = [int(p) for p in input("")[1 : -1].split(',')]
n = len(num)
tmp = []
for i in num :
    tmp.append(i)
    tmp.append(i << 1)
tmp = sorted(tmp)
rankList = [tmp[0]]
for i in range(1, n << 1) :
    if tmp[i-1] != tmp[i] :
        rankList.append(tmp[i])
m = len(rankList)

def getRank(x) :
    left = 0 ; right = m - 1
    while left < right :
        mid = (left + right) >> 1
        if x > rankList[mid] :
            left = mid + 1
        elif x < rankList[mid] :
            right = mid - 1
        else :
            return mid + 1
    return left + 1

t = [0] * (m+1)

def lowbit(x) :
    return x & (-x)

def query(i) :
    if i <= 0 :
        return 0
    return t[i] + query(i ^ lowbit(i))

def update(i, x) :
    if i > m :
        return
    t[i] += x
    update(i + lowbit(i), x)

ans = 0
for i in range(n-1, -1, -1) :
    ans += query(getRank(num[i]) - 1)
    update(getRank(num[i] << 1), 1)

print(ans)
