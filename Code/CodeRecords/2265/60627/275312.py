#include<stdio.h>

#include<cstring>

#include<algorithm>

using namespacestd;

const intMAXN=1000;

intfirst[MAXN],next[MAXN*MAXN],data[MAXN*MAXN],arcnum;

void add(int a,intb)

{

      arcnum++;

      data[arcnum]=b;

      next[arcnum]=first[a];

      first[a]=arcnum;

}

intlow[MAXN],dfn[MAXN],cnt=1,ans[MAXN],root;

void tarjan(int u)

{

      low[u]=dfn[u]=cnt++;

      int v,i,son=0;

      for(i=first[u];i!=0;i=next[i]){

           v=data[i];

           son++;

           if(dfn[v]==0){

                 tarjan(v);

                 if(low[u]>low[v])low[u]=low[v];

                 if((u==root&&son>=2)||(u!=root&&low[v]>=dfn[u]))ans[u]=1;

           }

           elseif(low[u]>dfn[v])low[u]=dfn[v];

      }

}

main()

{

      int n,i,num,a,b;

      char c;

      scanf("%d",&n);

      scanf("%c",&a);

      while(n!=0){

           memset(first,0,sizeof(first));

           memset(dfn,0,sizeof(dfn));

           memset(low,0,sizeof(low));

           memset(ans,0,sizeof(ans));

           scanf("%d",&a);

           while(a!=0)

           {

                 do{

                      scanf("%d",&b);

                      add(a,b);

                      add(b,a);

                      c=getchar();

                 }

                 while(c!='\n');

                 scanf("%d",&a);

           }

           root=1;

           tarjan(root);

           num=0;

           for(i=1;i<=n;i++){

                 if(ans[i]==1)num++;

           }

           printf("%d\n",num);

           scanf("%d",&n);

      }

     

}