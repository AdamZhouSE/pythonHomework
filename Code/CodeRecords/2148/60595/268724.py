#include <bits/stdc++.h>
using namespace std;
char s[25];
int t[105];
int sta1[105],sta2[105];
int res1[105],res2[105];
int dis[2100000],vis[2100000];
queue<int> Q;
int main()
{
    memset(dis,0x3f,sizeof(dis));
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i = 1;i <= m;++i){
        scanf("%d",&t[i]);
        scanf("%s",s);
        for(int j = 0;j < n;++j){
            if(s[j] == '+') sta1[i] += (1<<j);
            else if(s[j] == '-') sta2[i] += (1<<j);
        }
        scanf("%s",s);
        for(int j = 0;j < n;++j){
            if(s[j] == '+') res2[i] += (1<<j);
            else if(s[j] == '-') res1[i] += (1<<j);
        }
    }
    int now = (1<<n)-1;
    dis[now] = 0;
    Q.push(now);
    vis[now] = 1;
    while(!Q.empty()){
        now = Q.front();
        Q.pop();
    
        for(int i = 1;i <= m;++i){
            if((now & sta1[i]) != sta1[i]) continue;
            if((~now & sta2[i]) != sta2[i]) continue;
            int tmp = (now  & (~res1[i])) | res2[i];           
            if(dis[tmp] > dis[now] + t[i]){
                dis[tmp] = dis[now] + t[i];
                if(!vis[tmp]) vis[tmp] = 1,Q.push(tmp);
            }
        }
        vis[now] = 0;
    }
    if(dis[0] == 0x3f3f3f3f) puts("0");
    else printf("%d\n",dis[0]);
    return 0;
}