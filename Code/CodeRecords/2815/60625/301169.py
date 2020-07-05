#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
const int maxn=1e5+50;
ll n,zs,fs,zero,ans,t;
int main()
{
   cin>>n;
   ll ans=0;
   for(ll i=0;i<n;i++)
   {
      cin>>t;
      if(t==0) zero++;
      else if(t>=1){
        ans+=t-1;    zs++; //正数
      }
      else if(t<=-1){
        ans-=t+1;    fs++; //负数
      }
   }
   if(fs%2==0)
    ans+=zero;
   else{
    if(zero){ 
            ans+=1; zero--; ans+=zero;
    }
    else
        ans+=2;
   }
   cout<<ans<<endl;
    return 0;
}
 
 
 