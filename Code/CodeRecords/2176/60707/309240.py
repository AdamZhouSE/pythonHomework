#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#define ll long long
#define maxx 1000005
using namespace std;
int sa[maxx];
int tp[maxx];
int rak[maxx];
int tax[maxx];
char s[maxx];
int n,m;
void qSort()
{
    for(int i=0;i<=m;i++)tax[i]=0;
    for(int i=1;i<=n;i++)tax[rak[i]]++;
    for(int i=1;i<=m;i++)tax[i]+=tax[i-1];
    for(int i=n;i>=1;i--)sa[tax[rak[tp[i]]]--]=tp[i];
}
void suffix()
{
    m=75;
    for(int i=1;i<=n;i++)
        rak[i]=s[i]-'0',tp[i]=i;
    qSort();
    for(int w=1,p=0;p<n;m=p,w<<=1)
    {
        p=0;
        for(int i=1;i<=w;i++)tp[++p]=n-w+i;
        for(int i=1;i<=n;i++)if(sa[i]>w)tp[++p]=sa[i]-w;
        qSort();
        swap(tp,rak);
        rak[sa[1]]=p=1;
        for(int i=2;i<=n;i++)
            rak[sa[i]]=(tp[sa[i-1]]==tp[sa[i]]&&tp[sa[i-1]+w]==tp[sa[i]+w])?p:++p;
    }
}
int main()
{
    scanf("%s",s+1);
    n=strlen(s+1);
    suffix();
    for(int i=1;i<n;i++)printf("%d ",sa[i]);
    printf("%d\n",sa[n]);
    return 0;
}

