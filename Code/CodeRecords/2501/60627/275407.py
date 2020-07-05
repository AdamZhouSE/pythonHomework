#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#define int long long
#define N 100005
#define lowbit(x) (x & (-x))
using namespace std;
 
int n, ans;
int a[N], t[N];
map<string, int> mp;
 
void upd(int pos, int val)
{
    while(pos <= n)
    {
        t[pos] += val;
        pos += lowbit(pos);
    }
}
 
int ask(int pos)
{
    int res = 0;
    while(pos >= 1)
    {
        res += t[pos];
        pos -= lowbit(pos);
    }
    return res;
}
 
signed main()
{
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        string t; cin >> t;
        mp[t] = i;
    }
    for(int i = 1; i <= n; i++)
    {
        string t; cin >> t;
        a[i] = mp[t];
    }
    for(int i = 1; i <= n; i++)
    {
        upd(a[i], 1);
        ans += i - ask(a[i]);
    }
    cout << ans<<endl;
    return 0;
}