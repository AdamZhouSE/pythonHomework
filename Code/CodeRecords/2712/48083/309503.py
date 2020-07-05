#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
struct tree{
    int ch[26],cnt,fail;
}t[100001];
struct node{
    int next,to;
}w[150001];
int n,num,pos[200],sum[150001],heap,tail;
int head[150001],team[105001],cnt,maxn;
char ch[200][100],s[1000010];
inline void add(int x,int y){
    w[++cnt].next=head[x];
    w[cnt].to=y; head[x]=cnt;
}
inline void insert(int x){
    int u=0,l=strlen(ch[x]);
    for (int i=0; i<l; i++){
        int a=ch[x][i]-'a';
        if (!t[u].ch[a]) t[u].ch[a]=++num;
        u=t[u].ch[a];
    }
    t[u].cnt++; pos[x]=u;
}
inline void build(){
    heap=tail=1; team[heap]=0;
    while (heap<=tail){
        int x=team[heap];
        for (int i=0; i<26; i++){
            if (x==0){
                if (t[x].ch[i]){
                    t[t[x].ch[i]].fail=0;
                    team[++tail]=t[x].ch[i];
                }
                continue;
            }
            if (t[x].ch[i]){
                t[t[x].ch[i]].fail=t[t[x].fail].ch[i];
                team[++tail]=t[x].ch[i];
            }
            else t[x].ch[i]=t[t[x].fail].ch[i];
        }
        heap++;
    }
}
void dfs(int x){
    for (int i=head[x]; i; i=w[i].next){
        dfs(w[i].to); sum[x]+=sum[w[i].to];
    }
}
int main(){
    while (1){
        scanf("%d",&n);
        if (!n) return 0; num=0;
        memset(t,0,sizeof(t));
        memset(ch,0,sizeof(ch));
        memset(pos,0,sizeof(pos));
        memset(sum,0,sizeof(sum));
        memset(head,0,sizeof(head));
        for (int i=1; i<=n; i++){
            scanf("%s",ch[i]);
            insert(i);
        }
        build(); scanf("%s",s); cnt=0;
        for (int i=1; i<=num; i++){
            add(t[i].fail,i);
            // printf("%d %d\n",t[i].fail,i);
        }
        int u=0,l=strlen(s);
        for (int i=0; i<l; i++){
            int a=s[i]-'a';
            u=t[u].ch[a];
            sum[u]++;
        }
        dfs(0); maxn=0;
        for (int i=1; i<=n; i++)
            maxn=max(maxn,sum[pos[i]]);
        printf("%d\n",maxn);
        for (int i=1; i<=n; i++)
            if (sum[pos[i]]==maxn) printf("%s\n",ch[i]);
    }
    return 0;
}
