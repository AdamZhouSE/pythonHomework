a = [int(x) for x in input().split(",")]
b = [int(x) for x in input().split(",")]
m,n = len(a),len(b)
a.sort()
b.sort()
ans = -1
if m>n:
    a,b,m,n = b,a,n,m

imin,imax,half_len = 0,m,(m+n+1)//2
while imin<=imax:
    i = (imin + imax)//2
    j = half_len - i
    if i < m and b[j-1]>a[i]:
        imin = i+1
    elif i > 0 and a[i-1]>b[j]:
        imax = i-1
    else:
        if i == 0 : maxleft = b[j-1]
        elif j == 0: maxleft = a[i-1]
        else:maxleft = max(a[i-1],b[i-1])

        if (m+n)%2==1:
            ans = maxleft
            break
        if i == m: minright = b[j]
        elif j == n: minright = a[i]
        else:minright = min(a[i],b[j])

        ans = (maxleft+minright)/2
        break
print("{:.5f}".format(ans))