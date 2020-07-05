
#include<cstdio>

#include<iostream>

bool b[3001][3001];

int v[3001],f[3001],a[3001][3001];

int va[3001],du[3001],mc[3001],rd[3001],dfn[3001],low[3001],stack[3001];

int n,m,p,x,y,num,deep,nd,minn=1e9,tot;

inline int readint()

{

    int i=0,f=1;

    char ch;

    for(ch=getchar();ch<'0'||ch>'9';ch=getchar());

    for(;ch>='0' && ch<='9';ch=getchar())

        i=(i<<3)+(i<<1)+ch-'0';

    return i*f;

}

inline void put(int x)  

{  

    int num=0;char c[15];

    while(x) c[++num]=(x%10)+48,x/=10;

    while(num) putchar(c[num--]);

}

inline void zoom(int x)

{

	int list[3001],d=0,l=0,mini=1e9,mint=1e9;

	while(stack[num]!=x)

	{

		++l;

		list[l]=stack[num];

		f[stack[num]]=false;

		--num;

	}

	f[stack[num]]=false;

	++l;

	list[l]=stack[num];

	--num;

	for(int i=1;i<=l;++i)

	{

		mint=std::min(list[i],mint);

		d+=rd[list[i]];

		if(va[list[i]]>0&&va[list[i]]<mini) mini=va[list[i]];

	}

	for(int i=1;i<=l;++i)

		for(int j=1;j<=l;++j)

			if(i!=j&&b[list[i]][list[j]]) --d;

	if(!d&&mini==1e9) minn=mint;

	++nd;

	du[nd]=d;

	mc[nd]=mini;

}

inline void dfs(int x)

{

	low[x]=dfn[x]=++deep;

	stack[++num]=x;

	f[x]=true;

	for(int i=1;i<=a[x][0];++i)

		if(!v[a[x][i]])

		{

			v[a[x][i]]=true;

			dfs(a[x][i]);

			low[x]=std::min(low[x],low[a[x][i]]);

		}

		else if(f[a[x][i]]) low[x]=std::min(low[x],dfn[a[x][i]]);

	if(low[x]==dfn[x]) zoom(x);

}

inline void get()

{

	if(minn!=1e9)

	{

		puts("NO");

		put(minn);

	}

	else

	{

		for(int i=1;i<=nd;++i) if(!du[i]) tot+=mc[i];

		puts("YES");

		put(tot);

	}

}

int main()

{

	int i; 

	freopen("net.in","r",stdin);

	n=readint();

	p=readint();

	for(i=1;i<=p;++i) x=readint(),va[x]=readint();

	m=readint();

	for(i=1;i<=m;++i)

	{

		x=readint();

		y=readint();

		++a[x][0];

		a[x][a[x][0]]=y;

		b[x][y]=true;

		++rd[y];

	}

	for(i=1;i<=n;++i) if(!v[i]) dfs(i);

	get();

	return 0;

}
