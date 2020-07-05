#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
inline int rd(){
    int x=0,f=1;
    char ch=getchar();
    for(;!isdigit(ch);ch=getchar()) if(ch=='-') f=-1;
    for(;isdigit(ch);ch=getchar()) x=x*10+ch-'0';
    return x*f;
}
inline void write(int x){
    if(x<0) putchar('-'),x=-x;
    if(x>9) write(x/10);
    putchar(x%10+'0');
    return ;
}
int n,m,k;
int head[100006],nxt[100006],to[100006];
int total=0;
void add(int x,int y){
    total++;
    to[total]=y;
    nxt[total]=head[x];
    head[x]=total;
    return ;
}
int v[100006];
int dfn[100006];
int low[100006];
int tot=0;
int color[100006];
int book[100006];
int sta[100006],set=0;
int dis[100006];
int cnt=0;
void tarjan(int x){
    low[x]=dfn[x]=++tot;
    book[x]=1;
    sta[++set]=x;
    for(int e=head[x];e;e=nxt[e]){
        if(!dfn[to[e]]){
            tarjan(to[e]);
            low[x]=min(low[x],low[to[e]]);
        }
        else if(book[to[e]]) low[x]=min(low[x],dfn[to[e]]);
    }
    if(dfn[x]==low[x]){
        dis[++cnt]=min(dis[cnt],v[x]);
        color[x]=cnt;
        book[x]=0;
        while(set&&sta[set]!=x){
            dis[cnt]=min(dis[cnt],v[sta[set]]);
            color[sta[set]]=cnt;
            book[sta[set]]=0;
            set--;
        }
        set--;
    }
    return ;
}
int du[100006];
int main(){
    memset(dis,127,sizeof(dis));
    memset(v,127,sizeof(v));
    n=rd(),k=rd();
    for(int i=1;i<=k;i++){
        int x=rd();
        v[x]=rd();
    }
    m=rd();
    for(int i=1;i<=m;i++){
        int x=rd(),y=rd();
        add(x,y);
    }
    for(int i=1;i<=n;i++) if(!dfn[i]&&v[i]!=2139062143) tarjan(i);
    for(int i=1;i<=n;i++) if(!dfn[i]){
        printf("NO\n");
        write(i);
        return 0;
    }
    printf("YES\n");
    for(int i=1;i<=n;i++) for(int e=head[i];e;e=nxt[e]) if(color[i]!=color[to[e]]) du[color[to[e]]]++;
    int ans=0;
    for(int i=1;i<=cnt;i++) if(!du[i]) ans+=dis[i];
    write(ans);
    return 0;
}
