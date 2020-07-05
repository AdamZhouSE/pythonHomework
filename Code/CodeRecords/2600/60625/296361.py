#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#define N 20009
using namespace std;

int n;

struct W{
    double x,y;
}w[N];

bool cmp(W a,W b){
    if(a.x==b.x)return a.y<b.y;
    return a.x<b.x;
}

int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%lf%lf",&w[i].x,&w[i].y);
    }
    sort(w+1,w+n+1,cmp);
    double xx=(w[1].x+w[n].x)/2.0;
    double yy=(w[1].y+w[n].y)/2.0;
    for(int i=2;i<=n;i++){
        if(n-i+1<=i)break;
        double tx=(w[i].x+w[n-i+1].x)/2.0;
        double ty=(w[i].y+w[n-i+1].y)/2.0;
        if(tx!=xx||ty!=yy){
            printf("This is a dangerous situation!\n");
            return 0;
        }
    }
    printf("V.I.P. should stay at (%.1lf,%.1lf).",xx,yy);
    return 0;
}