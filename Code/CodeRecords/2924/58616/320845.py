#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

typedef __int64 LL;
const int maxn = 1e5 + 5;
struct node
{
    LL a, b;
}exam[maxn];

LL cmp(node x, node y)
{
    if (x.b == y.b)
        return x.a < y.a;
    return x.b < y.b;
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in.txt", "r", stdin);
    #endif // ONLINE_JUDGE
    LL n, r, avg;
    LL has, need, needed;

    while (scanf("%I64d%I64d%I64d", &n, &r, &avg) != EOF)
    {
        has = 0;
        for (__int64 i = 0; i < n; i++)
        {
            scanf("%I64d%I64d", &exam[i].a, &exam[i].b);
            has += exam[i].a;
        }

        sort(exam, exam+n, cmp);
        LL needed = 1ll * avg * n;
        LL need = 1ll*needed - 1ll*has;
        if (need <= 0)
            printf("0\n");
        else
        {
            LL ans = 0;
            for (LL i = 0; i < n && need > 0; i++)
            {
                if ((r-exam[i].a) <= need)
                {
                    ans += (r-exam[i].a) * exam[i].b;
                    need -= r-exam[i].a;
                }
                else
                {
                    ans += need * exam[i].b;
                    need -= need;
                }
            }
            printf("%I64d\n", ans);
        }
    }
    return 0;
}