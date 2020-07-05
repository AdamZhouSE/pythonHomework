
#include<map>
#include<set>
#include<ctime>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
set<int>s;
map<long long,bool>mp;
long long  num[100010],p[1000010],b[1000010],h[1000010];
int n,m,q;
 
int main()
{
	int i,j;
	srand(1289);
 
	scanf("%d%d%d\n",&n,&m,&q);
	for(i=1;i<=n;++i) num[i]=(long long)rand()*rand()%1000000000*(rand()*rand()%2000000000); 
	s.insert(1);
	for(i=1;i<=n;++i) h[1]^=num[i],p[1]++,b[i]=1;
	for(i=1;i<=q;++i) 
	 {
	    char c;
	 	int x,y;
	 	scanf("%c",&c);
	 	scanf("%d%d\n",&x,&y);
	 	if(c=='C')
	 	  {
	 	  	if(b[x]==y) continue;
	 	  	s.erase(b[x]); s.erase(y);
	 	  	
	 	    h[b[x]]^=num[x];
	 	    p[b[x]]--;
	 	    if (!mp[h[b[x]]]) s.insert(b[x]);
	 	    
	 	    h[y]^=num[x];
	 	    p[y]++;
	 	    if (!mp[h[y]]) s.insert(y);
	 	    
	 	    b[x]=y;
	 	  }
	 	 else
	 	  if(c=='W')
	 	   {
	 	     int ans=0;
			 set<int>::iterator it=s.lower_bound(x);
			 for(;it!=s.end()&&*it<=y;it=s.lower_bound(x))
			  {
			  	mp[h[*it]]=1;
			  	ans+=p[*it];
			  	s.erase(it);
			  }	
			 printf("%d\n",ans);
	 	  }
	 }
	 return 0;
}
