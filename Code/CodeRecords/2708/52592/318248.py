#include<iostream>
#include<cstdio>
#include<map>
#include<algorithm>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<set>
#define N 500000
#define LL long long
using namespace std;
int n,m,k,tree[N];
map<LL,LL> mp;
set<int> s;
LL num[N],hp[N];
int size[N],mark[N],pos[N];
int main()
{
	scanf("%d%d%d",&n,&m,&k);
	srand(2016+7+6);
	for (int i=1;i<=n;i++)
	{
		LL x,y,z;
		x=rand()*rand()%1000000000;
		y=rand()*rand()%2000000000;
		num[i]=(LL)x*y;
		hp[1]^=num[i];
		pos[i]=1;
	}
	mp.clear();
    size[1]=n; 
    s.insert(1);
	for (int i=1;i<=k;i++)
	{
		char s1[10];
		scanf("%s",s1);
		if (s1[0]=='C')
		{
			int x,y; scanf("%d%d",&x,&y);
			if (pos[x]==y) continue;
			s.erase(pos[x]);
			s.erase(y);
			hp[pos[x]]^=num[x]; size[pos[x]]--;
			if (mp[hp[pos[x]]]!=1)  s.insert(pos[x]);
			pos[x]=y; size[pos[x]]++;
			hp[pos[x]]^=num[x]; 
			if (mp[hp[pos[x]]]!=1) s.insert(pos[x]);
		}
		else
		{
			int x,y; scanf("%d%d",&x,&y);
			int ans=0;
			set<int>::iterator it=s.lower_bound(x);
			for (;it!=s.end()&&*it<=y;it=s.lower_bound(x))
			{
				mp[hp[*it]]=1;
				ans+=size[*it];
				s.erase(it);
			}
			printf("%d\n",ans);
		}
	}
}
