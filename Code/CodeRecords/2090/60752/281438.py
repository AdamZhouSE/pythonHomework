#include<iostream>
#include<cstdio>
#include<cstring>
#define maxn 210
using namespace std;
int n;
long long map[maxn][maxn],a[maxn][maxn],ans=1000000000000000;
void init(){
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            map[i][j]=a[i][j];
}
void floyed(){
    for(int k=1;k<=n;k++)
    for(int i=1;i<=n;i++)
    for(int j=1;j<=n;j++){
        if(i==j||j==k||i==k)continue;
        map[i][j]=min(map[i][j],map[i][k]+map[k][j]);
    }
}
long long count(){
    long long res=0;
    for(int i=1;i<=n;i++){
        for(int j=i+1;j<=n;j++)
        res=max(res,map[i][j]);
    }
    return res;
}
int main(){
    int l;
    while(1){
        scanf("%d%d",&n,&l);
        ans=1000000000000000;
        if(n==0&&l==0)return 0;
        int x,y,z;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if(i!=j)a[i][j]=10000000000000;
        for(int i=1;i<n;i++){
            scanf("%d%d%d",&x,&y,&z);
            a[x][y]=a[y][x]=z;
        }
        for(int i=1;i<=n;i++)
            for(int j=i+1;j<=n;j++){
                init();
                map[i][j]=min(map[i][j],1LL*l);
                map[j][i]=min(map[j][i],1LL*l);
                floyed();
                ans=min(ans,count());
            }
        cout<<ans<<endl;
    }
    return 0;
}
