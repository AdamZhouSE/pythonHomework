#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

int main()
{
    int n, a, p;
    while (~scanf("%d", &n))
    {
        int min = 101;int ans = 0;
        for (int i = 1; i <=n; i++)
        {
            scanf("%d%d", &a, &p);
            if (p <= min) ans += a*p,min = p;
            else ans += min*a;
        }
        printf("%d\n", ans);
    }
    return 0;
}