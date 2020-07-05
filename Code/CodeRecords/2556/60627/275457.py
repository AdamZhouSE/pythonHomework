#include<iostream>
#include<algorithm>
#include<cstdio>
#define maxn 50010
using namespace std;
int n,k;
struct node{int x,y;}s[maxn];
int ans=0,have;
bool cmp(node a,node b){return a.x<b.x;}
int abs(int x){
    if(x>=0)return x;
    return -x;
}
int main(){
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++)scanf("%d%d",&s[i].x,&s[i].y);
    sort(s+1,s+n+1,cmp);
    for(int i=2;i<=n;i++){
        int tmp=0;
        for(int j=i-1;j>=1;j--){
            tmp+=(s[j+1].x-s[j].x);
            if(tmp>=k)break;
            if(abs(s[i].y-s[j].y)<k){
                if(have){puts("-1");return 0;}
                have=1;
                ans=(k-tmp)*(k-abs(s[i].y-s[j].y));
            }
        }
    }
    printf("%d\n",ans);
    return 0;
}