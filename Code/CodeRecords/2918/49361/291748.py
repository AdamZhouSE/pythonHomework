#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define maxn 110
int a[maxn],vis[maxn];
int main()
{
int n;
while(~scanf("%d",&n))
{
int i;
memset(vis,0,sizeof(vis));
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
sort(a,a+n);
int tmp,m=n;
int ans=0;
while(m)
{
tmp=0;
for(i=0;i<n;i++)
{
if(tmp<=a[i]&&!vis[i])
{
vis[i]=1;
tmp++;
m--;
}
}
ans++;
}
printf("%d\n",ans);
}
return 0;
