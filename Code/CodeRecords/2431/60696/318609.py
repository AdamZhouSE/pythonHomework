#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<ctime>
using namespace std;
const int N=1000005;
int s,u1,v1,Cnt,fa[N],ans,x[N],y[N],p,cou;
struct Node{
    int u,v,w;
}Edge[N*2];
bool cmp(Node a,Node b){
    return a.w<b.w;
}
int find(int x){
    if(fa[x]!=x){
        fa[x]=find(fa[x]);
    }
    return fa[x];
}
void kruskal(){
    sort(Edge+1,Edge+1+cou,cmp);
    for(int i=1;i<=cou;i++){
        u1=find(Edge[i].u);
        v1=find(Edge[i].v);
        if(u1==v1){
            continue;
        }
        ans=Edge[i].w;
        fa[v1]=u1;
        Cnt++;
        if(Cnt==p-s){
			break;
		}
    }
}
int main(){
    scanf("%d%d",&s,&p);
    for(int i=1;i<=p;i++){
        scanf("%d%d",&x[i],&y[i]);
		for(int j=1;j<i;j++){
			int d=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]);
			Edge[++cou].u=i;
			Edge[cou].v=j;
			Edge[cou].w=d;
		}
    }
    for(int i=1;i<=p;i++){
        fa[i]=i;
    }
    kruskal();
	printf("%.2f",sqrt((double)ans));
    return 0;
}