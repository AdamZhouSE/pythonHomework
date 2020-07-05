
#include<iostream>

#include<cmath>

#include<cstdio>

#include<cstdlib>

#include<cstring>

#include<algorithm>

#define F(i,j,n) for(int i=j;i<=n;i++)

#define D(i,j,n) for(int i=j;i>=n;i--)

#define ll long long

#define N 200005

#define M 4000005

using namespace std;

int n,m;

int pos[N];

int last=1,cnt=1,a[N][26],fa[N][20],mx[N],c[N],q[N];

int tot,rt[N],ls[M],rs[M];

char s[N];

inline int read()

{

	int x=0,f=1;char ch=getchar();

	while (ch<'0'||ch>'9'){if (ch=='-') f=-1;ch=getchar();}

	while (ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}

	return x*f;

}

void insert(int &k,int l,int r,int x)

{

	k=++tot;

	if (l==r) return;

	int mid=(l+r)>>1;

	if (x<=mid) insert(ls[k],l,mid,x);

	else insert(rs[k],mid+1,r,x);

}

int merge(int x,int y)//线段树的合并 

{

	if (!x||!y) return x+y;

	int z=++tot;

	ls[z]=merge(ls[x],ls[y]);rs[z]=merge(rs[x],rs[y]);

	return z;

}

bool find(int k,int l,int r,int L,int R)

{

	if (!k) return 0;

	if (l==L&&r==R) return 1;

	int mid=(l+r)>>1;

	if (R<=mid) return find(ls[k],l,mid,L,R);

	else if (L>mid) return find(rs[k],mid+1,r,L,R);

	else return find(ls[k],l,mid,L,mid)||find(rs[k],mid+1,r,mid+1,R);

}

void add(int x,int id)

{

	int p=last,np=++cnt;last=np;

	mx[np]=mx[p]+1;pos[id]=np;insert(rt[np],1,n,id);

	while (p&&!a[p][x]) a[p][x]=np,p=fa[p][0];

	if (!p) fa[np][0]=1;

	else

	{

		int q=a[p][x];

		if (mx[q]==mx[p]+1) fa[np][0]=q;

		else

		{

			int nq=++cnt;mx[nq]=mx[p]+1;

			memcpy(a[nq],a[q],sizeof(a[q]));

			fa[nq][0]=fa[q][0];fa[np][0]=fa[q][0]=nq;

			while (a[p][x]==q) a[p][x]=nq,p=fa[p][0];

		}

	}

}

void calc()

{

	F(i,1,cnt) c[mx[i]]++;

	F(i,1,cnt) c[i]+=c[i-1];

	F(i,1,cnt) q[c[mx[i]]--]=i;

	D(i,cnt,1)

	{

		int x=q[i],f=fa[x][0];

		rt[f]=merge(rt[f],rt[x]);

	}

	F(j,1,18) F(i,1,cnt) fa[i][j]=fa[fa[i][j-1]][j-1];

}

bool check(int mid,int x,int l,int r)

{

	D(i,18,0) if (mx[fa[x][i]]>=mid) x=fa[x][i];

	return find(rt[x],1,n,l,r);

}

int main()

{

	n=read();m=read();

	scanf("%s",s+1);reverse(s+1,s+n+1);

	F(i,1,n) add(s[i]-'a',i);

	calc();

	F(i,1,m)

	{

		int a=n-read()+1,b=n-read()+1,c=n-read()+1,d=n-read()+1;

		swap(a,b);swap(c,d);

		int l=1,r=min(d-c+1,b-a+1),mid,ans=0;

		while (l<=r)

		{

			mid=(l+r)>>1;

			if (check(mid,pos[d],a+mid-1,b)) ans=mid,l=mid+1;

			else r=mid-1;

		}

		printf("%d\n",ans);

	}

	return 0;

}
