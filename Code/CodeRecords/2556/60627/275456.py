#include<cstdio>
#include<iostream>
#include<algorithm>
#define maxn 50010
using namespace std;
int n,k,ans;
struct node{
    int x,y;
}p[maxn];
bool cmp(node a,node b){
    if(a.x!=b.x)return a.x<b.x;
    return a.y<b.y;
}
int Abs(int x){
    if(x>=0)return x;
    return -x;
}
int check(int x,int y){
    int x1=p[x].x,x2=p[y].x;
    int y1=p[x].y,y2=p[y].y;
    if(x1==x2){
        if(y2-y1>=k)return 0;
        int d=y2-y1;
        return k*(k-d);
    }
    if(y1==y2){
        if(x2-x1>=k)return 0;
        int d=x2-x1;
        return k*(k-d);
    }
    if(Abs(x1-x2)>=k&&Abs(y1-y2)>=k)return 0;
    int mx1=max(x1-k/2,x2-k/2),mn1=min(x1+k/2,x2+k/2);
    int mx2=max(y1-k/2,y2-k/2),mn2=min(y1+k/2,y2+k/2);
    return (mx1-mn1)*(mx2-mn2);
}
int main(){
    freopen("Cola.txt","r",stdin);
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++)scanf("%d%d",&p[i].x,&p[i].y);
    sort(p+1,p+n+1,cmp);
    int t=0;
    for(int i=1;i<=n;i++){
        for(int j=i+1;j<=n;j++){
            int now=check(i,j);
            if(now>0){
                if(t>=1){
                    puts("-1");return 0;
                }
                ans+=now;
                t++;
            }
        }
    }
    if(ans)printf("%d\n",ans);
    else puts("0");
}