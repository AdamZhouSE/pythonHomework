#include<bits/stdc++.h>
using namespace std;
#if 0
#undef assert
#define assert(e) (void)(0)
int reads()
{
	char ch=getchar();
	while(!isdigit(ch)&&ch!='-')ch=getchar();
	int sign=1;
	if(ch=='-')
	{
		sign=-1;
		ch=getchar();
	}
	int value=ch-'0';
	ch=getchar();
	while(isdigit(ch))
	{
		value=value*10+ch-'0';
		ch=getchar();
	}
	return value*sign;
}
vector<string> v;
int k;
void dfs(int n, string s)
{
	if(n==0)return v.push_back(s);
	for(int i=0;i<k;++i)dfs(n-1,s+char('a'+i));
}
vector<int> get_rank(string s)
{
	vector<string> substr;
	for(int i=0;i<s.size();++i)substr.push_back(s.substr(i));
	sort(substr.begin(),substr.end());
	vector<int> rank(s.size(),-1);
	for(int i=0;i<s.size();++i)rank.at(s.size()-1-substr.at(i).size()+1)=i;
	for(int i=0;i<s.size();++i)assert(rank[i]>=0&&rank[i]<s.size());
	return rank;
}
long long fac(int n)
{
	if(n==1)return 1;
	return n*fac(n-1);
}
void find_missing(const set<vector<int> > &st, vector<int> v, int n,set<int> occ)
{
	assert(v.size()==occ.size());
	if(n==0)
	{
		assert(v.size()==occ.size());
		if(!st.empty())assert(v.size()==st.begin()->size());
		if(st.find(v)==st.end())
		{
			for(int i=0;i<v.size();++i)cout<<v.at(i)<<ends;
			cout<<"<---\n";
			cout<<"throw\n";
			throw 0;
		}
		return;
	}
	for(int i=0;i<n+v.size();++i)
	{
		if(occ.find(i)!=occ.end())continue;
		v.push_back(i);
		bool b=occ.insert(i).second;
		assert(b);
		assert(occ.find(i)!=occ.end());
		find_missing(st,v,n-1,occ);
		assert(!v.empty());
		v.pop_back();
		for(auto cur:occ)assert(occ.find(cur)!=occ.end());
		assert(occ.find(i)!=occ.end());
		occ.erase(occ.find(i));
		assert(v.size()==occ.size());
		for(int i=0;i<v.size();++i)assert(occ.find(v[i])!=occ.end());
	}
}
int main()
{
	k=1;
	while(k<=100)
	{
		cout<<k<<": ";
		int n=1;
		while(true)
		{
			dfs(n,"");
			set<vector<int> > st;
			for(int i=0;i<v.size();++i)
			{
				string s=v[i];
				st.insert(get_rank(s));
			}
			v.clear();
			if(st.size()!=fac(n))
			{
				try
				{
					cout<<"call n="<<n<<endl;
					find_missing(st,vector<int>(),n,set<int>());
				}
				catch(int){}
				goto next_k;
			}
			++n;
		}
		next_k:
		++k;
	}
}
#endif
int main()
{
	int k;
	cin>>k;
	printf("%d\n",k+1);
	for(int i=0-1;i<k;++i)
	if((k-i)&1)printf("%d ",k-(k-i)/2+1);
	else printf("%d ",(k-i)/2-1+1);
	puts("");
	return 0; 
}