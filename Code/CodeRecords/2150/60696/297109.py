#include<cstdio>
#include<cstring>
#include<algorithm>
#define cl(x,y) memset(x,y,sizeof(x))
using namespace std;

const int maxn=25,maxs=60005,INF=0x3f3f3f3f;
int n,m,q,g[maxn][maxn],f[maxn][maxs],p3[maxn];
int s[maxn],t[maxn],l[maxn],r[maxn],ans;
int main(){
    scanf("%d%d%d",&n,&m,&q);
    cl(g,63);for (int i=1;i<=n;i++) g[i][i]=0;
    for (int i=1,x,y,z;i<=m;i++)
     scanf("%d%d%d",&x,&y,&z),g[x][y]=min(g[x][y],z);
    for (int i=0;i<q;i++) scanf("%d%d%d%d",&s[i],&t[i],&l[i],&r[i]);
    for (int k=1;k<=n;k++)
     for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++)
       if (k!=i&&i!=j&&j!=k) g[i][j]=min(g[i][k]+g[k][j],g[i][j]);
    p3[0]=1;for (int i=1;i<=q;i++) p3[i]=p3[i-1]*3;

    cl(f,63);
    f[1][0]=0;
    for (int S=0;S<p3[q];S++)
     for (int i=1;i<=n;i++)
      if (f[i][S]!=INF){
        int tot=0;
        for (int j=0;j<q;j++){
            int T=S/p3[j]%3;
            if (T==0){
                f[s[j]][S+p3[j]]=min(f[s[j]][S+p3[j]],max(f[i][S]+g[i][s[j]],l[j]));
            }else
            if (T==1){
                if (f[i][S]+g[i][t[j]]<=r[j])
                 f[t[j]][S+p3[j]]=min(f[t[j]][S+p3[j]],f[i][S]+g[i][t[j]]);
            }else tot++;
        }
        ans=max(ans,tot);
      }
    printf("%d",ans);
    return 0;
}