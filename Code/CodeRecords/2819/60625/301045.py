#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
int n,a[5],ans=0,k;
int main()
{
    memset(a,0,sizeof(a));
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&k);
        a[k]++;
    } 
    ans+=a[4]+a[2]/2;
    a[2]%=2;
    k=min(a[1],a[3]);
    ans+=k;
    a[1]-=k;
    a[3]-=k;
    if(a[3]!=0) ans+=a[3];
    if(a[1]!=0)
    {
        ans+=a[1]/4;
        a[1]%=4;
    }
    k=a[1]+a[2]*2;
    if(k<=4&&k!=0) ans++;
    else if(k!=0) ans+=2;
    cout<<ans<<endl;
    return 0;
}