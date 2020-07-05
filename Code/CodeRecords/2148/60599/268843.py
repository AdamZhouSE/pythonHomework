#include<bits/stdc++.h>
using namespace std;
const int M=100+5;
const int N=22;

int n, m;
char s1[30], s2[30];
int dist[1<<N];
bool vis[1<<N];
void out(int);

struct fix{
    int b1, b2, f1, f2, t;
}a[M];

int spfa(){
    memset(dist,127,sizeof(dist));
    queue <int> q; int s = (1<<n)-1 , inf = dist[0], nx;
    dist[s] = 0; vis[s] = 1; q.push(s);
    while(!q.empty()){//求最短路
    int x = q.front(); q.pop(); vis[x] = 0;
    for(int i=1;i<=m;i++){
        if(((~x)&a[i].b1) != 0) continue;
        if((x&a[i].b2) != 0) continue;//这两个判断与b1,b2的关系
        nx = (x | a[i].f2);
        nx = (nx & (~a[i].f1));//如果可以打该补丁，则得到新状态nx，进行松弛
        if(dist[nx] > dist[x] + a[i].t){
        dist[nx] = dist[x]+a[i].t;
        if(!vis[nx]) vis[nx] = 1 , q.push(nx);
        }
    }
    }
    return dist[0]==inf?0:dist[0];
}

int main(){
    //freopen("data.in","r",stdin);
    int x; cin >> n >> m;
    for(int i=1;i<=m;i++){
    scanf("%d%s%s",&x,s1,s2);
    a[i].t = x;
    for(int j=0;j<n;j++){
        if(s1[j] == '+') a[i].b1 += 1<<n-j-1;//读入并压成二进制
        if(s1[j] == '-') a[i].b2 += 1<<n-j-1;
        if(s2[j] == '+') a[i].f2 += 1<<n-j-1;
        if(s2[j] == '-') a[i].f1 += 1<<n-j-1;
    }
    }
    printf("%d\n",spfa());
    return 0;
}