  #include<cstdio>
  #include<iostream>
  using namespace std;
  int n,m,dfn[16005],tim,low[16005],fir[16005],l[40005],to[40005],cnt;
  int sta[40005],top,ins[40005],bel[40005],cnt_scc,al[40005];
  void link(int a,int b){l[++cnt]=fir[a];fir[a]=cnt;to[cnt]=b;}
  void tarjan(int p){
      dfn[p]=low[p]=++tim;sta[++top]=p;ins[p]=1;
      for(int i=fir[p];i;i=l[i])if(!dfn[to[i]])tarjan(to[i]),low[p]=min(low[p],low[to[i]]);
         else if(ins[to[i]])low[p]=min(low[p],dfn[to[i]]);
     if(low[p]==dfn[p]){
         cnt_scc++;
         do{ins[sta[top]]=0;bel[sta[top]]=cnt_scc;top--;}while(sta[top+1]!=p);
     }
 }
 int main(){
     scanf("%d%d",&n,&m);n<<=1;
     for(int i=1,x,y;i<=m;++i)scanf("%d%d",&x,&y),link(x+1,y+1^1),link(y+1,x+1^1);
     for(int i=2;i<=n+1;++i)if(!dfn[i])tarjan(i);
     for(int i=2;i<=n;i+=2)if(bel[i]==bel[i^1]){puts("NIE");return 0;}
     for(int i=2;i<=n;i+=2)printf("%d\n",(i^bel[i]>bel[i^1])-1);
 }