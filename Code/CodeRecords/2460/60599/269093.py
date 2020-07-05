#include<iostream>
#include<cstdio>
#include<algorithm>
#include<queue>

using namespace std;

typedef long long ll;
const int maxn=100050;

int n;
ll f[maxn],d[maxn],ind[maxn],min_tree[maxn],now[maxn];
// f[i]父亲节点 d[i]要求物品数 c[i]花费 ind[i]入度 min_tree[i]子树中物品最小花费 now[i]当前物品数 
ll ans=0;

void read(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%lld%lld%lld",&f[i],&d[i],&min_tree[i]);
        if(f[i]!=-1)ind[f[i]]++;
    }
}

void work(){
    queue<int> q;
    for(int i=1;i<=n;i++)
        if(ind[i]==0)q.push(i);
    while(!q.empty()){
        int t=q.front();
        if(d[t]>now[t])ans+=1ll*min_tree[t]*(d[t]-now[t]);
        if(t!=1){
        min_tree[f[t]]=min(min_tree[f[t]],min_tree[t]);
        ind[f[t]]--;
        now[f[t]]+=max(d[t],now[t]);    
        if(ind[f[t]]==0)q.push(f[t]);
        }

        q.pop();
    }
}

void print(){
    printf("%lld\n",ans);
}

int main(){
    read();
    work();
    print();
}