#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int a[110];
int main()
{
    int n,i,j,x;
    cin>>n;
    memset(a,0,sizeof(a));
    for(i=0;i<n;i++)
    {
        cin>>x;
        a[x]++;
    }
    int ans=-1;
    for(i=1;i<=100;i++)
    {
        ans = max(ans,a[i]);
    }
    cout<<ans<<endl;
    return 0;
}