#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std; 
typedef long long ll;
const int N = 10000;
const int B = 105;
const int Maxn = 1e9;

int n, m, bnum;
ll a[N + 5], an[N + 5], pos[N + 5], l[B], r[B];

template <typename T>
inline void read(T &X) {
    X = 0;
    char ch = 0;
    T op = 1;
    for(; ch > '9' || ch < '0'; ch = getchar())
        if(ch == '-') op = -1;
    for(; ch >= '0' && ch <= '9'; ch = getchar())
        X = (X << 3) + (X << 1) + ch - 48;
    X *= op; 
}

inline void modify(int x, ll c) {
    a[x] = c;
    for(int i = l[pos[x]]; i <= r[pos[x]]; i++)
        an[i] = a[i];
    sort(an + l[pos[x]], an + r[pos[x]] + 1);
}

inline ll getNum(int b, ll v) {
    ll ln = l[b], rn = r[b], mid;
    for(; ln <= rn;) {
        mid = (ln + rn) >> 1;
        if(an[mid] < v) ln = mid + 1;
        else rn = mid - 1;
    }
    return ln - l[b]; 
}

inline ll cnt(int x, int y, ll v) {
    ll res = 0;
    if(pos[x] == pos[y]) {
        for(int i = x; i <= y; i++)
            if(a[i] < v)
                res++;
    } else {
        for(int i = x; i <= r[pos[x]]; i++) 
            if(a[i] < v)
                res++;

        for(int i = l[pos[y]]; i <= y; i++) 
            if(a[i] < v)
                res++;

        for(int i = pos[x] + 1; i <= pos[y] - 1; i++) 
            res += getNum(i, v);
    }
    return res;
}

inline ll query(int x, int y, ll c) {
    ll ln = 0, rn = Maxn, mid, res = 0;
    for(; ln <= rn;) {
        mid = (ln + rn) >> 1;
        if(cnt(x, y, mid) < c) ln = mid + 1;
        else {
            rn = mid - 1;
            res = mid;
        }
    }
    return res - 1;
}

int main() {
    read(n), read(m);
    for(int i = 1; i <= n; i++) {
        read(a[i]);
        an[i] = a[i];
    }

    bnum = sqrt(n);
    for(int i = 1; i <= bnum; i++) {
        l[i] = (i - 1) * bnum + 1;
        r[i] = i * bnum;
    }
    if(r[bnum] < n) {
        r[++bnum] = n;
        l[bnum] = r[bnum - 1] + 1;
    }
    for(int i = 1; i <= bnum; i++) {
        for(int j = l[i]; j <= r[i]; j++)
            pos[j] = i;
        sort(an + l[i], an + r[i] + 1);
    }   

    for(char op[5]; m--;) {
        scanf("%s", op);
        if(op[0] == 'C') {
            int x, v;
            read(x), read(v);
            modify(x, v);
        } else {
            int x, y, c;
            read(x), read(y), read(c);
            printf("%lld\n", query(x, y, c));
        }
    }
    return 0;
}