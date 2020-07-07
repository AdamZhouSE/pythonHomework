#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
int n;
string s[30008];
int ch[300008][28],num,ind[28];
bool vis[300008],used[28][28],f;
int ans[30008],num_ans;
int nume,head[28],to[908],nxt[908];
deque<int> q;
inline void addedge(int x,int y)
{
    ++nume;to[nume]=y;nxt[nume]=head[x];head[x]=nume;
}
inline void update(string x)
{
    int u=0,t;
    for(int i=0;i<x.size();i++){
        t=x[i]-'a';
        if(!ch[u][t]){
            ch[u][t]=++num;
        }
        u=ch[u][t];
    }
    vis[u]=1;
}
inline void solve(string x)
{
    int u=0,t;
    for(int i=0;i<x.size();i++){
        t=x[i]-'a';
        if(vis[u]){
            f=1;
            return;
        }
        for(int j=0;j<26;j++){
            if(ch[u][j]&&j!=t&&!used[t][j]){
                used[t][j]=1;
                addedge(t,j);
                ind[j]++;
            }
        }
        u=ch[u][t];
    }
}
inline bool ok()
{
    for(int i=0;i<26;i++){
        if(!ind[i])    q.push_back(i);
    }
    while(!q.empty()){
        int now=q.front();q.pop_front();
        for(int i=head[now];i;i=nxt[i]){
            ind[to[i]]--;
            if(!ind[to[i]]){
                q.push_back(to[i]);
            }
        }
    }
    for(int i=0;i<26;i++){
        if(ind[i]){
            return 0;
        }
    }
    return 1;
}
int main()
{
    ios::sync_with_stdio(false);
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>s[i];
        update(s[i]);
    }
    for(int i=1;i<=n;i++){
        nume=0;
        q.clear();
        f=0;
        memset(head,0,sizeof(head));
        memset(ind,0,sizeof(ind));
        memset(used,0,sizeof(used));
        solve(s[i]);
        if(f)    continue;
        if(ok())    ans[++num_ans]=i;
    }
    printf("%d\n",num_ans);
    for(int i=1;i<=num_ans;i++){
        printf("%s\n",s[ans[i]].c_str());
    }
    return 0;
}