#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;
struct node
{int fa,deep;}tr[200];
int n,ans=1,sum=0;//ans是深度sum是宽度
int dep[200];
int main()
{
    int i,u,v;
    cin>>n;tr[1].deep=1;dep[1]=1;
    for(i=1;i<n;i++)
    {
        cin>>u>>v;
        tr[v].fa=u;
        tr[v].deep=tr[u].deep+1;
        if(tr[v].deep>ans)ans=tr[v].deep;
       
        dep[tr[v].deep]++;
    }
    cin>>u>>v;
    for(i=1;i<=ans;i++)
     if(dep[i]>sum)sum=dep[i];
    cout<<ans<<endl<<sum<<endl;
    if(u==v){cout<<0;return 0;}
    int depp1=0,depp2=0;
    while(tr[u].fa!=tr[v].fa)
    {
        if(tr[u].fa==v){cout<<(depp1+1)*2;return 0;}
        if(tr[v].fa==u){cout<<depp2+1;return 0;}
        if(tr[u].deep>tr[v].deep){depp1++;u=tr[u].fa;}
        if(tr[v].deep>tr[u].deep){depp2++;v=tr[v].fa;}
        if(tr[u].deep==tr[v].deep&&tr[u].fa!=tr[v].fa)
        {depp1++;u=tr[u].fa;depp2++;v=tr[v].fa;}
    }
    cout<<(depp1+1)*2+depp2+1;
   
    return 0;
}