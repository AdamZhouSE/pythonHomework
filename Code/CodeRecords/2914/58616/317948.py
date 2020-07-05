#include <bits/stdc++.h>
using namespace std;
#define SIS std::ios::sync_with_stdio(false),cin.tie(0),cout.tie(0)
#define endl '\n'
#define ll long long
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fLL;
const int MAXN = 1e5+5;
int a[MAXN],b[MAXN];

int main()
{
    SIS;
    int T;
    cin >> T;
    while(T--)
    {
        int n;
        bool flag=false;
        cin >> n;
        for(int i=0;i<n;i++) cin >> a[i];
        for(int i=0;i<n;i++)
        {
            cin >> b[i];
            a[i]=b[i]-a[i];
            if(a[i]<0) flag=true;
        }
        int p1=-1,p2=-1;
        for(int i=0;i<n;i++)
        {
            if(a[i])
            {
                if(p1==-1) p1=i;
                p2=i;
            }
        }
        if(p1!=-1)
        {
            int x=a[p1];
            for(int i=p1;i<=p2;i++)
            {
                if(x!=a[i]) flag=true;
            }
        }
        if(flag) cout << "NO" << endl;
        else cout << "YES" << endl;
    }
    return 0;
}