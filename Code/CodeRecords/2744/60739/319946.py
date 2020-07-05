#include<bits/stdc++.h>
#define ll long long
#define u unsigned int
using namespace std;
const u bas=233;
int n,m;
u hsh[2000100],now,k[2000100];
char a[2000100];
u hh(int l,int r){return hsh[r]-hsh[l-1]*k[r-l+1];}
bool pd(int x)
{//cout<<now<<" "<<x<<endl;
    for(register int i=1;i<=m;i+=x){//cout<<hh(i,i+x-1)<<" ";
    if(hh(i,i+x-1)!=now)return 0;}return 1;
}
main()
{
    scanf("%d",&n);k[0]=1;
    multiset<u>s;for(int i=1;i<=2e6;i++)k[i]=k[i-1]*bas;
    for(int ii=1;ii<=n;ii++)
    {
        scanf("%d",&m);
        scanf("%s",a+1);
        for(int i=1;i<=m;i++)
        hsh[i]=hsh[i-1]*bas+a[i];
        for(int i=1;i<=m;i++)
        {
            if(m%i)continue;
            now=hh(1,i);
            if(pd(i))
            {//cout<<endl;
                s.insert(now);break;
            }//cout<<endl;
        }
    }
    ll ans=0;
    while(!s.empty())
    {
        int o=*s.lower_bound(0),oo=s.count(o);//cout<<oo<<endl;
        ans+=(ll)oo*oo;s.erase(o);
    }cout<<ans<<endl;
}