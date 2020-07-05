#include <cstdio>
#include <algorithm>

const int N=50;
int T,Cnt[1<<22],n,m,Ans;
int a[N],l[N],r[N],c[N],b[N],st[N],Last[N];

void DFS(int x,int S,int tot)
{
    if(tot>=Ans)
        return;
    if(x==m){
        Ans=tot;
        return;
    }
    int s=Cnt[st[x]&S];
    DFS(x+1,S|(1<<x),tot+std::min(s,b[x]-s));
    if(x)
        DFS(x+1,S,tot+std::min(c[x]-s,b[x]-c[x]+s));
}

int main()
{
    for(int i=1;i<1<<22;++i)
        Cnt[i]=Cnt[i>>1]+(i&1);
    for(scanf("%d",&T);T--;)
    {
        scanf("%d",&n),m=0,Ans=1e9;
        for(int i=1;i<=n;++i)
            scanf("%d",&a[i]),Last[i]=b[i]=c[i]=st[i]=0;
        for(int i=n;i>=1;--i)
            if(!Last[a[i]])
                Last[a[i]]=i;
            else 
                l[m]=i,r[m]=Last[a[i]],++m;
        std::reverse(l,l+m),std::reverse(r,r+m);
        for(int i=0;i<m;++i){
            for(int j=0;j<i;++j){
                if(r[j]>l[i]){
                    ++b[i];
                    if(r[j]<r[i])
                        st[i]|=1<<j,++c[i];
                }
            }
        }
        DFS(0,0,0);
        printf("%d\n",Ans);
    }
    return 0;
}