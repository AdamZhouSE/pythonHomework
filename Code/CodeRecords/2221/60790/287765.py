
#include<iostream>

#include<cstdio>

#include<cstring>

#include<algorithm>

#define N 500003

using namespace std;

int n,m,x[N],y[N];

int dfsn[N],low[N],next[N],point[N],v[N],ins[N];

int belong[N],st[N],top,tot,sz,cnt,size[N],mark[N];

void add(int x,int y)

{

	tot++; next[tot]=point[x]; point[x]=tot; v[tot]=y;

}

void tarjan(int x)

{

	st[++top]=x; ins[x]=1;

	dfsn[x]=low[x]=++sz;

	for (int i=point[x];i;i=next[i])

	 {

	 	int j=v[i];

	 	if (!dfsn[j]){

	 		tarjan(j);

	 		low[x]=min(low[x],low[j]);

	 	}

	 	else if (ins[j])  low[x]=min(dfsn[j],low[x]);

	 }

	int j;

	if (low[x]==dfsn[x]){

		cnt++;

		do

		{

			j=st[top--];

			ins[j]=0;

			belong[j]=cnt;

			size[cnt]++;

		}while (j!=x);

	}

}

int main()

{

	scanf("%d%d",&n,&m);

	memset(dfsn,0,sizeof(dfsn));

	memset(low,0,sizeof(low));

	for (int i=1;i<=m;i++)

	{

		scanf("%d%d",&x[i],&y[i]);

		add(x[i],y[i]);

	}

	memset(ins,0,sizeof(ins));

	for (int i=1;i<=n;i++)

	 if (!dfsn[i]) tarjan(i);

	for (int i=1;i<=m;i++)

	 if (belong[x[i]]!=belong[y[i]]){

	 	mark[belong[x[i]]]++;

	 }

	int total=0;

	for (int i=1;i<=cnt;i++)

	 if (!mark[i]) {

	   if (total) {

	   	printf("0\n");

	   	return 0;

	   }

	   total=i;

	 }

	printf("%d\n",size[total]);

}
