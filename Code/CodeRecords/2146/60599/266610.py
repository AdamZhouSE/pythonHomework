#include<bits/stdc++.h>
using namespace std;
#define pi pair<int,int>
#define mp make_pair
#define fi first
#define se second
#define N 10005
queue<pi >q;
struct ji{
    int nex,to,len;
}edge[N*20];
int E,t,n,m,k,x,y,z,ans,d[N][41],vis[N][41],head[N],p[N];
void add(int x,int y,int z){
    edge[E].nex=head[x];
    edge[E].to=y;
    edge[E].len=z;
    head[x]=E++;
}
int main(){
    scanf("%d",&t);
    while (t--){
        scanf("%d%d%d",&n,&m,&k);
        memset(d,0x3f,sizeof(d));
        memset(head,-1,sizeof(head));
        memset(vis,0,sizeof(vis));
        E=0;
        for(int i=1;i<=n;i++){
            scanf("%d",&p[i]);
            p[i]=p[i]*2-3;
        }
        for(int i=1;i<=m;i++){
            scanf("%d%d%d",&x,&y,&z);
            add(x,y,z);
            add(y,x,z);
        }
        scanf("%d%d",&x,&y);
        d[x][p[x]+20]=0;
        vis[x][p[x]+20]=1;
        q.push(mp(x,p[x]+20));
        while (!q.empty()){
            pi o=q.front();
            q.pop();
            vis[o.fi][o.se]=0;
            for(int i=head[o.fi];i!=-1;i=edge[i].nex){
                x=edge[i].to;
                if ((abs(o.se+p[x]-20)<=k)&&(d[o.fi][o.se]+edge[i].len<d[x][o.se+p[x]])){
                    d[x][o.se+p[x]]=d[o.fi][o.se]+edge[i].len;
                    if (!vis[x][o.se+p[x]]){
                        q.push(mp(x,o.se+p[x]));
                        vis[x][o.se+p[x]]=1;
                    }
                }
            }
        }
        ans=0x3f3f3f3f;
        for(int i=20-k;i<=k+20;i++)ans=min(ans,d[y][i]);
        if (ans==0x3f3f3f3f)ans=-1;
        printf("%d\n",ans);
    }
}