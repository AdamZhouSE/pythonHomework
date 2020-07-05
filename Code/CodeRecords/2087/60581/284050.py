#include<cstdio>
#include<iostream>
#define N 501
using namespace std;
typedef long long LL;
int n;
LL a[N],b[N];
bool g[N][N],vis[N];
int match[N];
void read(int &x)
{
    x=0; int f=1; char c=getchar();
    while(!isdigit(c)) { if(c=='-') f=-1;  c=getchar(); }
    while(isdigit(c)) { x=x*10+c-'0'; c=getchar(); }
    x*=f;
}
void read(LL &x)
{
    x=0; int f=1; char c=getchar();
    while(!isdigit(c)) { if(c=='-') f=-1;  c=getchar(); }
    while(isdigit(c)) { x=x*10+c-'0'; c=getchar(); }
    x*=f;
}
inline LL gcd(LL p,LL q) { return !q ? p : gcd(q,p%q); }
bool go(int now)
{
    for(int i=1;i<=b[0];i++)
    {
        if(vis[i] || !g[now][i]) continue;
        vis[i]=true;
        if(!match[i] || go(match[i]))
        {
            match[i]=now;
            return true;
        }
    }
    return false;
}
int main()
{
    read(n);
    LL x;
    for(int i=1;i<=n;i++)
    {
        read(x);
        (x&1 ? a[++a[0]] : b[++b[0]])=x;
    }
    for(int i=1;i<=a[0];i++)
        for(int j=1;j<=b[0];j++)
            if(gcd(a[i],b[j])==1 && gcd(a[i]+1,b[j]+1)==1) g[i][j]=true;
    int sum=0;
    for(int i=1;i<=a[0];i++)
    {
        fill(vis+1,vis+b[0]+1,0);
        if(go(i)) sum++;
    }
    printf("%d",n-sum); 
}