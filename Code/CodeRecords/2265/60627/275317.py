#include<iostream>
 #include<stdio.h>
 #include<vector>
 #include<string.h>
 #include<stdlib.h>
 using namespace std;
 ;
 int dfn[maxn], low[maxn];
 int cut[maxn];
 int n,m,num,sol;
 vector<int> g[maxn];
 void init()
 {
     memset(dfn,,sizeof(dfn));
     memset(cut,,sizeof(cut));
     ;i<=n;i++) g[i].clear();
     num=sol=;
 }
 void tarjan(int u,int fa)
 {
     ;
     dfn[u] = low[u] = ++num;
     ;i<g[u].size();i++)
     {
         int v=g[u][i];
         if (!dfn[v])
         {
             children++;
             tarjan(v,u);
             low[u] = min(low[u], low[v]);
              && children >= )||(fa != - && low[v] >= dfn[u]))
                 cut[u]=;
         }
         else if (v != fa)
             low[u] = min(low[u], dfn[v]);
     }
 }
 int main()
 {
     while(scanf("%d",&n)!=EOF&&n)
     {
         int x,y;
         init();
         while(scanf("%d",&x)&&x)
         {
             while(getchar()!='\n')
             {
                 scanf("%d",&y);
                 g[x].push_back(y);
                 g[y].push_back(x);
             }
         }
         tarjan(,-);
         ;i<=n;i++)
             if(cut[i])sol++;
         printf("%d\n",sol);
     }
 }