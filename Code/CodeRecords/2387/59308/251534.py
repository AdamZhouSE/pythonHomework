import re
pattern = re.compile('-*[0-9]+')
a = [int(x) for x in pattern.findall(input())]
n = a[0]
m = a[1]
a = [int(x) for x in pattern.findall(input())]
for i in range(m):
    b = [int(x) for x in pattern.findall(input())]
    op = b[0]
    ll = b[1]
    rr = b[2]
    if op == 0:
        b = sorted(a[ll-1:rr])
        for j in range(ll-1, rr):
            a[j] = b[j-ll+1]
    else:
        b = sorted(a[ll - 1:rr], reverse=True)
        for j in range(ll - 1, rr):
            a[j] = b[j - ll + 1]
q = int(input())
print(a[q-1])


