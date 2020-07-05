#include <bits/stdc++.h>

#define ll long long

#define sc scanf

#define pr printf

using namespace std;

ll gcd(ll a, ll b)

{

    return b == 0 ? a : gcd(b, a % b);

}

int main()

{

    int n;

    scanf("%d", &n);

    ll t1, t2;

    sc("%lld", &t1);

    for (int i = 1; i < n; i++)

    {

        sc("%lld", &t2);

        t1 = gcd(t1, t2);

    }

    ll qq = sqrt(t1);

    ll ans = 0;

    for (ll i = 1; i <= qq; i++)

    {

        if (t1 % i == 0)

        {

            ans++;

            if (t1 / i != i)

                ans++;

        }

    }

    printf("%lld", ans);
    printf("\n", ans);

}