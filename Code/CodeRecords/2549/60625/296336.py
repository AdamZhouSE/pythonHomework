#include <iostream>
#include <cstdio>
#include <cstdlib>
#define N 100000 + 30000 + 5
#define inf 0x7fffffff
using namespace std;

struct T {int l, r, cnt, size, val, dat;} t[N];
int n, q, root, tot, sum;

int read()
{
    int x = 0, f = 1; char c = getchar();
    while(c < '0' || c > '9') {if(c == '-') f = -1; c = getchar();}
    while(c >= '0' && c <= '9') {x = x * 10 + c - '0'; c = getchar();}
    return x *= f;
}

int New(int val)
{
    t[++tot].val = val, t[tot].dat = rand();
    t[tot].size = t[tot].cnt = 1;
    return tot;
}

void up(int p) {t[p].size = t[t[p].l].size + t[t[p].r].size + t[p].cnt;}

void zig(int &y)
{
    int x = t[y].l;
    t[y].l = t[x].r, t[x].r = y, y = x;
    up(t[y].r), up(y);
}

void zag(int &x)
{
    int y = t[x].r;
    t[x].r = t[y].l, t[y].l = x, x = y;
    up(t[x].l), up(x);
}

void insert(int &p, int val)
{
    if(!p) {p = New(val); return;}
    if(val == t[p].val) {t[p].cnt++, up(p); return;}
    if(val < t[p].val)
    {
        insert(t[p].l, val);
        if(t[t[p].l].dat > t[p].dat) zig(p);
    }
    else
    {
        insert(t[p].r, val);
        if(t[t[p].r].dat > t[p].dat) zag(p);
    }
    up(p);
}

int valOfRank(int p, int rank)
{
    if(!p) return inf;
    if(t[t[p].l].size >= rank) return valOfRank(t[p].l, rank);
    if(t[t[p].l].size + t[p].cnt >= rank) return t[p].val;
    return valOfRank(t[p].r, rank - t[t[p].l].size - t[p].cnt);
}

int main()
{
    New(inf), New(-inf), root = 1, t[1].l = 2, up(1);
    n = read(), q = read(), sum = n;
    for(int i = 1; i <= n; i++) insert(root, read());
    for(int i = 1; i <= q; i++)
    {
        int op = read(), x = read();
        if(op == 1) x = sum - x + 1, printf("%d\n", valOfRank(root, x + 1));
        else if(op == 2) insert(root, x), sum++;
    }
    return 0;
}