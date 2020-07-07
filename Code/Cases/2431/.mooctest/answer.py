#include<bits/stdc++.h>
    #define reint register int
    using namespace std;
    const int N=505;
    struct P1{
        int t1,t2;double v;
    }line[N*N];
    struct po{
        double x,y;
    }st[N];
    int s,p,num,fa[N];double ans;
    inline double dis(int x1,int y1){
        return sqrt((st[x1].x-st[y1].x)*
                    (st[x1].x-st[y1].x)+
                    (st[x1].y-st[y1].y)*
                    (st[x1].y-st[y1].y));
    }
    inline bool cmp(P1 x,P1 y){
        return x.v<y.v;
    }
    int find(int x){
        if(x!=fa[x])fa[x]=find(fa[x]);
        return fa[x];
    }
    inline void unionn(int x,int y)  {  
        fa[find(x)]=find(y);  
    }
    int main(){
        scanf("%d%d",&s,&p);
        for(reint i=1;i<=p;i++)fa[i]=i;
        for(reint i=1;i<=p;i++){
            scanf("%lf",&st[i].x);
            scanf("%lf",&st[i].y);
        }
        for(reint i=1;i<=p;i++)
        for(reint j=i+1;j<=p;j++){
            num++;
            line[num].t1=i;
            line[num].t2=j;
            line[num].v=dis(i,j);
        }
        sort(line+1,line+num+1,cmp);
        int a,b;s=p-s;
        for(reint i=1;i<=num,s>0;i++){
            a=line[i].t1;b=line[i].t2;
            if(find(a)!=find(b)){
                unionn(a,b);s--;
                ans=max(ans,line[i].v);    
            }
        }
        printf("%.2lf",ans);
        return 0;
}