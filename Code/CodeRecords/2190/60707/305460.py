#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
const int INF=1e9+7,MAXN=2e5+7,MAXC=26;
int nxt[MAXN][MAXC],link[MAXN],len[MAXN],lst,sz,siz[MAXN];
inline void extend(int c){
    int cur=++sz,p=lst;
    len[cur]=len[p]+1;
    siz[cur]=1;
    while(p!=-1&&!nxt[p][c]){
        nxt[p][c]=cur;
        p=link[p];
    }
    if(p==-1)
        link[cur]=0;
    else{
        int q=nxt[p][c];
        if(len[q]==len[p]+1)
            link[cur]=q;
        else{
            int clone=++sz;
            len[clone]=len[p]+1;
            memcpy(nxt[clone],nxt[q],sizeof(nxt[clone]));
            link[clone]=link[q];
            while(p!=-1&&nxt[p][c]==q){
                nxt[p][c]=clone;
                p=link[p];
            }
            link[q]=link[cur]=clone;
        }
    }
    lst=cur;
}
int tp,head[MAXN],to[MAXN],nxt_[MAXN];
inline void add(int x,int y){
    nxt_[++tp]=head[x];
    head[x]=tp;
    to[tp]=y;
}
int K,ans[MAXN];
void dfs(int x){
    for(int i=head[x];i;i=nxt_[i]){
        dfs(to[i]);
        siz[x]+=siz[to[i]];
    }
    if(x&&siz[x]==K){
        ans[len[link[x]]+1]++;
        ans[len[x]+1]--;
    }
}
char str[MAXN];
int M;
int Case;
int main(){
    scanf("%d",&Case);
    while(Case--){
        lst=sz=tp=0;
        link[0]=-1;
        scanf("%s%d",str+1,&K);
        M=strlen(str+1);
        for(int i=1;i<=M;i++)
            extend(str[i]-'a'),siz[lst]=1;
        for(int i=1;i<=sz;i++)
            add(link[i],i);
        dfs(0);
        for(int i=1;i<=M;i++)
            ans[i]+=ans[i-1];
        int maxi=0;
        for(int i=M;i>=1;i--)
            if(ans[i]>ans[maxi])
                maxi=i;
        printf("%d\n",maxi?maxi:-1);
        for(int i=0;i<=sz;i++){
            len[i]=siz[i]=link[i]=0;
        }
        memset(head,0,sizeof(head));
        memset(ans,0,sizeof(ans));
        memset(nxt,0,sizeof(nxt));
    }
    return 0;
}