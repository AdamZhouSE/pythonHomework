#include <bits/stdc++.h>
using namespace std;

#if __cplusplus < 201103 || !defined(__cplusplus)
typedef map<int,int> maptype;
#else
typedef unordered_map<int,int> maptype; // 如果是C++11及以上，使用无序哈希映射
#endif

struct edge
{
    int to,nxt;
};

edge e[1000001]; int head[10001],tot;
int in[10001];
maptype mapping;
char str[10001][105];
int len[10001];
int cnt[10001][26];
int f[10001];
int pre[10001];
int n;

void connect(int x,int y){
    e[++tot]=(edge){y,head[x]}; head[x]=tot; ++in[y];
}

int gethash(int idx){ 
    int val=0;
    for(register int i=0;i<26;++i){
        val=val*23+cnt[idx][i];
    }
    return val;
}

void output(int d){ 
    if(pre[d]!=0){
        output(pre[d]);
    }
    printf("%s\n",str[d]+1);
}

void topology(){ 
    queue<int> q;
    for(register int i=1;i<=n;++i){
        if(!in[i]) q.push(i);
        f[i]=1;
    }
    while(!q.empty()){
        int x=q.front(); q.pop();
        for(register int i=head[x],y;y=e[i].to,i;i=e[i].nxt){
            if(f[y]<f[x]+1){
                f[y]=f[x]+1;
                pre[y]=x;
            }
            if(--in[y]==0){
                q.push(y);
            }
        }
    }
    int ans=0;
    for(register int i=1;i<=n;++i){
        if(f[ans]<f[i]){
            ans=i;
        }
    }
    printf("%d\n",f[ans]);
    output(ans);
}

void build(){ //建边
    for(register int i=1;i<=n;++i){
        for(register int j=0;j<26;++j){
            ++cnt[i][j];
            int h=gethash(i);
            if(mapping.find(h)!=mapping.end()){ 
                connect(i,mapping[h]);
            }
            --cnt[i][j]; 
        }
    }
}

void input(){
    while(scanf("%s",str[++n]+1)!=EOF); --n; 
    for(register int i=1;i<=n;++i){
        len[i]=strlen(str[i]+1);
        for(register int j=1;j<=len[i];++j){
            ++cnt[i][str[i][j]-'a'];
        }
        mapping[gethash(i)]=i;
    }
}

int main(){
    input();
    build();
    topology();
    return 0;
}