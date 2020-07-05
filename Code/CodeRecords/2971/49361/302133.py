maxN = 1000010;
a = [];
rk = [];
sa = [];
tp = [];
tax = [];
for i in range(maxN):
    a.append(0);
    rk.append(0);
    sa.append(0);
    tp.append(0);
    tax.append(0);
s = input();
n = len(s);
for i in range(n):
    a[i+1] = s[i];
m = 122;
def  resort():
    for i in range(m+1):
        tax[i] = 0;
    for i in range(1, n+1):
        tax[rk[tp[i]]] += 1;
    for i in range(1, m+1):
        tax[i] += tax[i-1];
    for i in range(n, 0, -1):
        sa[tax[rk[tp[i]]]] = tp[i];
        tax[rk[tp[i]]] -= 1;


#suffix
for i in range(1, n+1):
    rk[i] = ord(a[i]);
    tp[i] = i;
resort();
k = 1;
while k <= n:
    num = 0;
    for i in range(n-k+1, n+1):
        num += 1;
        tp[num] = i;
    for i in range(1, n+1):
        if sa[i] > k:
            num+= 1;
            tp[num] = sa[i]-k;
    resort();
    tmp = rk;
    tk = tp;
    tp = tmp;
    rk[sa[1]] = 1;
    num = 1;
    for i in range(2, n+1):
        if tp[sa[i]]==tp[sa[i-1]] and tp[sa[i]+k]==tp[sa[i-1]+k]:
            rk[sa[i]] = num;
        else:
            num += 1;
            rk[sa[i]] = num;
    if num == n:
        break;
    m = num;
    k <<=1;
for i in range(1, n+1):
    print(sa[i], end=' '); 


