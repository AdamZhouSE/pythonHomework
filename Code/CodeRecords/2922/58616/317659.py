#include <bits/stdc++.h>

using namespace std;
typedef long long LL;
const int MAXN = 100000;
int arv[MAXN + 3];

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n; cin >> n;
    for(int i = 0; i < n; i++) cin >> arv[i];
    sort(arv, arv + n);
    int jud[MAXN + 3], len = 0;
    jud[len++] = arv[0];
    for(int i = 1; i < n; i++) if(arv[i] != arv[i - 1]) jud[len++] = arv[i];
    if(len == 1 || len == 2  || (len == 3 && jud[2] + jud[0] == jud[1] * 2) ) cout << "YES" << endl;
    else cout << "NO" << endl;
    return 0;
}