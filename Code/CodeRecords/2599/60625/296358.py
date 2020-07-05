#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int inf = 0x7ffffff;

int n,m,minn[300010],flag[300010],ans;
bool flag2 = false;

struct node
{
    int a,b;    
}e[100010];

bool cmp(node x,node y)
{
    if (x.b != y.b)
    return x.b < y.b;
    else
    return x.a > y.a;
}

void pushup(int o)
{
    minn[o] = min(minn[o * 2],minn[o * 2 + 1]);
}

void pushdown(int o)
{
    if (flag[o])
    {
        flag[o * 2] += flag[o];
        flag[o * 2 + 1] += flag[o];
        minn[o * 2] -= flag[o];
        minn[o * 2 + 1] -= flag[o];
    }
    flag[o] = 0;
}

void build(int l,int r,int o)
{
    if (l == r)
    {
        scanf("%d",&minn[o]);
        return;
    }
    int mid = (l + r) >> 1;
    build(l,mid,o * 2);
    build(mid + 1,r,o * 2 + 1);
    pushup(o);
}

void update(int l,int r,int o,int x,int y)
{
    if (x <= l && r <= y)
    {
        flag[o]++;
        minn[o]--;
        return;
    }
    pushdown(o);
    int mid = (l + r) >> 1;
    if (x <= mid)
    update(l,mid,o * 2,x,y);
    if (y > mid)
    update(mid + 1,r,o * 2 + 1,x,y);
    pushup(o);
}

int query(int l,int r,int o,int x,int y)
{
    if (x <= l && r <= y)
    return minn[o];
    pushdown(o);
    int mid = (l + r) >> 1,res = inf;
    if (x <= mid)
    res = min(query(l,mid,o * 2,x,y),res);
    if (y > mid)
    res = min(query(mid + 1,r,o * 2 + 1,x,y),res);
    return res;
}

int main()
{
    scanf("%d%d",&n,&m);
    build(1,n,1);
    for (int i = 1; i <= m; i++)
    scanf("%d%d",&e[i].a,&e[i].b);
    sort(e + 1,e + 1 + m,cmp);
    for (int i = 1; i <= m; i++)
    {
        if (query(1,n,1,e[i].a,e[i].b) <= 0)
        continue;
        update(1,n,1,e[i].a,e[i].b);
        ans++;
    }
    printf("%d\n",ans);
    
    return 0;
}