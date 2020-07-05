#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    int a[105];
    cin >> t;
    while(t--)
    {
        int n;
        cin >> n;
        int ans = 0;
        int a1 = 0,a2 = 0;
        for(int i = 0;i < n;i++)
        {
            cin >> a[i];
            a[i] %= 3;
            if(a[i] == 0) ans++;
            else if(a[i] == 1) a1++;
            else if(a[i] == 2) a2++;
        }
        if(a1 == a2) cout << ans + a1 << endl;
        else
        {
            int m = min(a1,a2);
            ans += m +(a1+a2-2*m)/3;
            cout << ans << endl;
        }
    }
    return 0;
}