#include <bits/stdc++.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
const int INF = 1e9;
const double eps = 1e-6;
//const int N = ;
int cas = 1;

ll n,r,avg,sum;

void run()
{
    ll a,b;
    vector<pii> v;
    sum = avg * n;
    for(int i = 0; i < n; i++ )
    {
        cin >> a >> b;
        sum -= a;
        v.push_back(make_pair(b,r-a));
    }
    sort(v.begin(),v.end());
    ll ans = 0;
    for(int i = 0; i < n; i++ )
    {
        if(sum <= 0) break;
        if(sum >= v[i].second)
            ans+=v[i].first*v[i].second, sum-=v[i].second;
        else
            ans += sum*v[i].first, sum -= sum;
    }
    cout << ans << endl;
}

int main()
{
    #ifdef LOCAL
//    freopen("case.txt","r",stdin);
    #endif
    while(cin >> n >> r >> avg)
        run();
    return 0;
}