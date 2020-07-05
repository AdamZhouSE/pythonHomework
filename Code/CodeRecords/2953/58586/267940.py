#include<bits/stdc++.h>

#define inf 0x7fffffff
#define LL long long
using namespace std;

LL n,ans;
LL calc(LL a,LL b){
    if(b==1) return a-1;
    if(!b) return inf;
    return a/b+calc(b,a%b);
}
int main()
{
    scanf("%lld",&n);
    ans=inf;
    for(LL i=1;i<=(n+1)>>1;i++)
        ans=min(ans,calc(n,i));
    
    printf("%lld",ans);
    
    return 0;
}