#include <cstdio>
#include <cstring>
#include <algorithm>
const int N=2e5+10;
char s[N];
int sa[N],Rank[N],tax[N],sec[N],n,m;
void Qsort()
{
    for(int i=1;i<=m;i++) tax[i]=0;
    for(int i=1;i<=n;i++) ++tax[Rank[i]];
    for(int i=2;i<=m;i++) tax[i]+=tax[i-1];
    for(int i=n;i;i--) sa[tax[Rank[sec[i]]]--]=sec[i];
}
bool cmp(int x,int y,int l){return sec[x]==sec[y]&&sec[x+l]==sec[y+l];}
void SuffixSort()
{
    scanf("%s",s+1);n=strlen(s+1);
    for(int i=1;i<=n;i++) Rank[i]=Rank[i+n]=s[i+n]=s[i],sec[i]=i,sec[i+n]=i+n;
    m=128,n<<=1;Qsort();
    for(int p=0,w=1;p<n;w<<=1,m=p)
    {
        p=0;for(int i=n-w+1;i<=n;i++) sec[++p]=i;
        for(int i=1;i<=n;i++) if(sa[i]>w) sec[++p]=sa[i]-w;
        Qsort();std::swap(Rank,sec);
        Rank[sa[1]]=p=1;
        for(int i=2;i<=n;i++) Rank[sa[i]]=cmp(sa[i],sa[i-1],w)?p:++p;
    }
}
int main()
{
    SuffixSort();
    for(int i=1;i<=n;i++)
        if(sa[i]<=n>>1)
            printf("%c",s[sa[i]+(n>>1)-1]);
    return 0;
}