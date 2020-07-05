#include <cstdio>
#include <cstring>

const int N = 100007;

int q, t;
int c2t = 0, t2t = 0;
char c;

int len[N];

struct Tree
{
    int rst[N], lson[N << 5], rson[N << 5];
    char val[N << 5];

    void build(int &rst, int fa, int l, int r, int po)
    {
        if (!rst)
            rst = ++t2t; 
        if (l == r)
        {
            val[rst] = c; 
            return;
        }
        int mid = (l + r) >> 1;
        if (po <= mid)
            rson[rst] = rson[fa], build(lson[rst], lson[fa], l, mid, po);
        if (mid + 1 <= po)
            lson[rst] = lson[fa], build(rson[rst], rson[fa], mid + 1, r, po);
    }

    char query(int rst, int l, int r, int po)
    {
        if (l == r)
            return val[rst]; 
        int mid = (l + r) >> 1;
        if (po <= mid)
            return query(lson[rst], l, mid, po);
        if (mid + 1 <= po)
            return query(rson[rst], mid + 1, r, po);
    }
} tree;

int main()
{
    scanf("%d", &q);
    while (q--)
    {
        scanf(" %c", &c);
        if (c == 'T')
        {
            scanf(" %c", &c);
            len[++c2t] = len[c2t - 1] + 1; 
            tree.build(tree.rst[c2t], tree.rst[c2t - 1], 1, N, len[c2t]);
        }
        else if (c == 'U')
        {
            scanf("%d", &t);
            len[++c2t] = len[c2t - t - 1]; 
            tree.rst[c2t] = tree.rst[c2t- t - 1];
        }
        else
        {
            scanf("%d", &t);
            printf("%c\n", tree.query(tree.rst[c2t], 1, N, t)); 
        }
    }
    return 0;
}