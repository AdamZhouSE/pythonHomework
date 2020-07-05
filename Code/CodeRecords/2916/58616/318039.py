#include<bits/stdc++.h>
#include<bits/extc++.h>
#define oo INT_MAX
#define ll long long
#define db double
#define mp(a, b) make_pair(a, b)
#define met(a, b) memset(a, b, sizeof(a))
#define maxn 500009
#define _rep(i, a, b) for(int i = (a); i <= (b); ++i)
#define _rev(i, a, b) for(int i = (a); i >= (b); --i)
#define _for(i, a, b) for(int i = (a); i < (b) ;++i)
using namespace std;
using namespace __gnu_pbds;
int n, a[maxn], cnt[maxn];
int main(){
    ios::sync_with_stdio(0);
    int n;
    cin >> n;
    _rep(i, 1, n){
        cin >> a[i];
        if(a[i] == 4)a[i] = 1;
        else if(a[i] == 8) a[i] = 2;
        else if(a[i] == 15) a[i] = 3;
        else if(a[i] == 16) a[i] = 4;
        else if(a[i] == 23) a[i] = 5;
        else a[i] = 6;
    }
    _rep(i, 1, n){
        _rep(j, 1, 6){
            if(a[i] == j && (j == 1 || cnt[j - 1] > cnt[j]))cnt[j] ++;
        }
    }
    cout << n - cnt[6] * 6 << endl;
    //system("pause");
}