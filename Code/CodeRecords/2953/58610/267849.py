#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<queue>
#define LL long long
using namespace std;
inline LL read() {
    LL d=0,f=1;char s=getchar();
    while(s<'0'||s>'9'){if(s=='-')f=-1;s=getchar();}
    while(s>='0'&&s<='9'){d=d*10+s-'0';s=getchar();}
    return d*f;
}
int ans=99999999;
int gcd(int x,int y)
{
    if(y==1) return x-1;
    if(x==0||y==0||x==y) return 99999999;
    return gcd(y,x%y)+x/y;
}
int main()
{     
    int n=read();
    ans=n-1;
    for(int i=2;i<=n;i++)
        ans=min(ans,gcd(n,i));
    printf("%d",ans);
    return 0;
}