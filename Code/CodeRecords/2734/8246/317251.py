#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;
const int N=1000005;

int n,c,m,size,color[N],Times[N],now,ans[N];
struct Ques
{
    int l,r,id;
}q[N];

int read()
{
    int now=0;char c=getchar();
    while(c<'0'||c>'9')c=getchar();
    while(c>='0'&&c<='9')now=(now<<3)+(now<<1)+c-'0',c=getchar();
    return now;
}

bool cmp(Ques a,Ques b)
{
    if(a.l/size == b.l/size) return a.r < b.r;
    return a.l/size < b.l/size;
}

inline void Add(int p)
{
    ++Times[p];
    if(Times[p]==2)
      ++now;
}
inline void Subd(int p)
{
    --Times[p];
    if(Times[p]==1)
      --now;
}

int main()
{
    n=read();c=read();m=read();
    size=sqrt(n);
    for(int i=1;i<=n;i++)
      color[i]=read();
    for(int i=1;i<=m;i++)
      q[i].l=read(),q[i].r=read(),q[i].id=i;
    sort(q+1,q+1+m,cmp);
    for(int i=1,l=1,r=0;i<=m;i++)
    {
        int ln=q[i].l,rn=q[i].r;
        while(l>ln)
          Add(color[--l]);
        while(l<ln)
          Subd(color[l++]);
        while(r<rn)
          Add(color[++r]);
        while(r>rn)
          Subd(color[r--]);
        ans[q[i].id]=now;
    }
    for(int i=1;i<=m;i++)
      printf("%d\n",ans[i]);
    return 0;
}