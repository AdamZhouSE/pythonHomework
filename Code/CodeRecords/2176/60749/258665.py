#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<bitset>
#include<set>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<ctime>
#include<algorithm>
#define ll long long
#define db double
#define inf 1<<30
#define maxn 1000005
#define eps 1e-8
using namespace std;
 
int n,m,a[maxn],c[maxn],sa[maxn],tp[maxn],rnk[maxn],hei[maxn];
char s[maxn];
 
void srt()
{
    ;i<=m;++i)c[i]=;
    ;i<=n;++i)c[rnk[tp[i]]]++;
    ;i<=m;++i)c[i]+=c[i-];
    for(int i=n;i;i--)sa[c[rnk[tp[i]]]--]=tp[i];
}
 
bool cmp(int *f,int x,int y,int w){return f[x]==f[y]&&f[x+w]==f[y+w];}
 
void getsa()
{
    ;i<=n;++i)rnk[i]=a[i],tp[i]=i;
    m=;srt();
    ,ln=;p<n;ln+=ln,m=p)
    {
        p=;
        ;i<=n;++i)tp[++p]=i;
        ;i<=n;++i)if(sa[i]>ln)tp[++p]=sa[i]-ln;
        srt();swap(tp,rnk);rnk[sa[]]=p=;
        ;i<=n;++i)rnk[sa[i]]=cmp(tp,sa[i],sa[i-],ln)?p:++p;
    }
    ,j;
    ;i<=n;hei[rnk[i++]]=k)
        :k,j=sa[rnk[i]-];a[j+k]==a[i+k];k++);
}
 
int main()
{
    scanf();
    n=strlen(s+);
    ;i<=n;++i)a[i]=s[i];
    getsa();
    ;i<=n;++i)printf("%d ",sa[i]);
    ;
}