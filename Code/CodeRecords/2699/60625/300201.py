#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;
struct Node{
    int son[27],end;
}N[300010];
vector<int> E[27];
int n,cnt=1,ind[30010],ans_sum,used[27][27];
string ans[30010],s[30010];
void insert(string s){
    int now=1;
    for(int i=0;i<s.length();i++){
        if(!N[now].son[s[i]-'a']) N[now].son[s[i]-'a']=++cnt;
        now=N[now].son[s[i]-'a'];
    }
    N[now].end++;
}
int work(string s){
    int now=1;
    for(int i=0;i<s.length();i++){
        int t=s[i]-'a';
        if(N[now].end) return 0;
        for(int j=0;j<26;j++){
            if(N[now].son[j]&&t!=j){
                E[t].push_back(j);
                ind[j]++;
            }
        }
        now=N[now].son[t];
    }
    return 1;
}
int check(){
    queue<int> q;
    for(int i=0;i<26;i++) if(!ind[i]) q.push(i);
    while(!q.empty()){
        int u=q.front(); q.pop();
        for(int i=0;i<E[u].size();i++){
            ind[E[u][i]]--;
            if(!ind[E[u][i]]) q.push(E[u][i]);
        }
    }
    for(int i=0;i<26;i++) if(ind[i]) return 0;
    return 1;
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        cin>>s[i];
        insert(s[i]);//建字典树 
    }
    for(int i=1;i<=n;i++){
        memset(used,0,sizeof(used));
        memset(ind,0,sizeof(ind));
        for(int j=0;j<27;j++) E[j].clear(); 
        if(!work(s[i])) continue;//如果有人是它的前缀返回0，直接不干了，如果没有，顺便建好图，准备接下来拓扑排序 
        if(check()) ans[++ans_sum]=s[i];//如果符合拓扑序 记录答案 
    }
    printf("%d\n",ans_sum);
    for(int i=1;i<=ans_sum;i++) cout<<ans[i]<<endl; 
    return 0;
}