#include<cstdio>
#include<cctype>
#include<cstring>
#include<iostream>
using namespace std;
const int N=2000005,base=233;
typedef unsigned long long ull;

int n,len[N],t[N][27],sz,val[N],belong[N];
//belong[i]:i这个节点属于哪个串的 
//注意总长不会超过N，即节点数也不会超过N 
//val[N*27] 过大导致一直RE。。 
ull p[N],Hash[N];
string s[N];
char tmp[N];

inline int read()
{
    int now=0,f=1;char c=getchar();
    for(;!isdigit(c);c=getchar())
      if(c=='-') f=-1;
    for(;isdigit(c);c=getchar())
      now=(now<<3)+(now<<1)+c-'0';
    return now*f;
}

void Pre()
{
    p[0]=1;
    for(int i=1;i<=2000000;++i)
        p[i]=p[i-1]*base;
}

int main()
{
    Pre();
    n=read();
    for(int i=1;i<=n;++i)
    {
        len[i]=read();
        scanf("%s",tmp);s[i]=tmp;//这样读string会快 
//    TLE:cin>>tmp;
        int u=0;
        ull v=0;
        for(int j=0;j<len[i];++j)
        {
            int id=s[i][j]-'a';
            if(!t[u][id])
                t[u][id]=++sz;
            u=t[u][id];
            v=v*base+(ull)(id+1);
        }
        ++val[u],belong[u]=i,Hash[i]=v;
    }
    long long res=0;
    for(int i=1;i<=n;++i)
    {
        int u=0;
        for(int j=0;j<len[i];++j)
        {
            u=t[u][s[i][j]-'a'];
            if(val[u] && Hash[belong[u]]*p[len[i]]+Hash[i]==Hash[i]*p[len[belong[u]]]+Hash[belong[u]])
                res+=val[u];
        }
    }
    printf("%lld\n",res*2-n);

    return 0;
}