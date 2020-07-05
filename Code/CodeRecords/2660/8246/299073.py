#include <cstdio>
#include <iostream>
#define ll long long

using namespace std;

ll read(){
    ll x = 0; int zf = 1; char ch = ' ';
    while (ch != '-' && (ch < '0' || ch > '9')) ch = getchar();
    if (ch == '-') zf = -1, ch = getchar();
    while (ch >= '0' && ch <= '9') x = x * 10 + ch - '0', ch = getchar(); return x * zf;
}

int s[20000005];
int ls[20000005], rs[20000005];
int len[20000005];
int rt[20000005], pre[20000005];
int tot;

inline void a(int pos){
    s[pos] = s[ls[pos]] + s[rs[pos]];
}

inline int getNew(){
    return (++tot);
}

void build(int pos, int l, int r){
    if (l == r){
        if (pos > tot)
            tot = pos;
        s[pos] = 0;
        return ;
    }
    int mid = (l + r) >> 1;
    ls[pos] = pos << 1, rs[pos] = (pos << 1) + 1;
    build(pos << 1, l, mid);
    build((pos << 1) + 1, mid + 1, r);
    a(pos);
}

int query(int pos, int l, int r, int k){
    if (l == r)
        return s[pos];
    int mid = (l + r) >> 1;
    if (k <= mid)
        return query(ls[pos], l, mid, k);
    else
        return query(rs[pos], mid + 1, r, k);
}

void add(int pos, int pre, int l, int r, int k, int val){
    if (l == r){
        s[pos] = val;
        return ;
    }
    int mid = (l + r) >> 1;
    if (k <= mid){
        rs[pos] = rs[pre]; ls[pos] = getNew();
        add(ls[pos], ls[pre], l, mid, k, val);
    }
    else{
        ls[pos] = ls[pre]; rs[pos] = getNew();
        add(rs[pos], rs[pre], mid + 1, r, k, val);
    }
    a(pos);
}

int main(){
    freopen("type.in", "r", stdin);
    freopen("type.out", "w", stdout);
    int q;
    q = read();
    rt[0] = 1, len[0] = 0;
    build(rt[0], 1, 100000);
    char op; int num; int rt_num = 0;
    for (int i = 1; i <= q; ++i){
        cin >> op;
        if (op == 'T'){
            char c; cin >> c;
            rt[++rt_num] = getNew();
            len[rt_num] = len[rt_num - 1] + 1;
            add(rt[rt_num], rt[rt_num - 1], 1, 100000, len[rt_num], (int)(c));
        }
        else if (op == 'Q'){
            num = read();
            printf("%c\n", (char)(query(rt[rt_num], 1, 100000, num)));
        }
        else if (op == 'U'){
            num = read(), ++rt_num;
            rt[rt_num] = rt[((rt_num - num - 1) > 0 ? (rt_num - num - 1) : 0)];
            ls[rt_num] = ls[((rt_num - num - 1) > 0 ? (rt_num - num - 1) : 0)], rs[rt_num] = rs[((rt_num - num - 1) > 0 ? (rt_num - num - 1) : 0)];
            len[rt_num] = len[rt_num - num - 1];
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}