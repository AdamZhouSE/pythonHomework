#include<bits/stdc++.h>
using namespace std;
#define ms(x, n) memset(x,n,sizeof(x));
typedef  long long LL;
const int INF = 1 << 30;
const int MAXN = 1e5+10;

int n, a[MAXN], b[MAXN];
bool used[MAXN];
int main() {
    ios::sync_with_stdio(false);
    cin >> n;
    for(int i = 1; i <= n; ++i)
        cin >> a[i];
    for(int i = 1; i <= n; ++i)
        cin >> b[i];
    int ans = 0;
    for(int i = 1, j = 1; i <= n && j <= n;){
        if(used[a[i]]){
            ++i;
            continue;
        }if(a[i] == b[j])
            ++j, ++i;
        else
            used[b[j]] = true, ++ans, ++j;

    }
    cout << ans << endl;

    return 0;
}