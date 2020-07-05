def doubling(s):
    n = len(s)
    sa = []
    rk = []
    for i in range(n):
        rk.append(ord(s[i])) 
        sa.append(i)
    l = 0 
    sig = 127 
    while l < n:
        p = []
        for i in range(n-l, n):
            p.append(i)
        for i in range(n):
            if sa[i] >= l:
                p.append(sa[i]-l)
        cnt = [0] * sig
        for i in range(n):
            cnt[rk[i]] += 1
        for i in range(1, sig):
            cnt[i] += cnt[i - 1]
        
        for i in range(n - 1, -1, -1):
            cnt[rk[p[i]]] -= 1
            sa[cnt[rk[p[i]]]] = p[i]
        def equal(i, j, l):
            if rk[i] != rk[j]:
                return False
            if i + l >= n and j + n >= n:
                return True
            if i + l < n and j + l < n:
                return rk[i + l] == rk[j + l]
            return False
        sig = -1
        tmp = [0] * n
        for i in range(n):
            if i == 0 or not equal(sa[i], sa[i - 1], l):
                sig += 1
            tmp[sa[i]] = sig
        rk = tmp
        sig += 1
        l = l << 1 if l > 0 else 1
    return [i+1 for i in sa]
if __name__=="__main__":
    res=doubling(input())
    print(*res)