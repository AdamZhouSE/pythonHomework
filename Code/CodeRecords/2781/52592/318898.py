#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
 
int len,d=0;
char aa[20];
bool kkk=false,a;
struct node{int end,s[3];}tr[1010];
 
void bt(char ss[],int s)
{
	int now=0; bool q=false;
	for(int i=1;i<=s;i++)
	{
		if(tr[now].s[ss[i]-'0'])
		{
			now=tr[now].s[ss[i]-'0'];
			if(tr[now].end) a=true;
		}
		else
		{
			len++; tr[now].s[ss[i]-'0']=len;
			now=len; tr[now].end=0; q=true;
		}
	}
	tr[now].end++;
	if(!q) a=true;
}
 
int main()
{
	//freopen("a.out","w",stdout);
	while(1)
	{
		a=false; len=0; d++;
		memset(tr[0].s,0,sizeof(tr[0].s));
		while(1)
		{
			if(scanf("%s",aa+1)==EOF) return 0;
			if((strlen(aa+1)==1)&&aa[1]=='9') break;
			bt(aa,strlen(aa+1));
		}
		if(a) printf("Set %d is not immediately decodable\n",d);
		else printf("Set %d is immediately decodable\n",d);
		for(int i=1;i<=len;i++)
		{
			for(int j=0;j<=1;j++) tr[i].s[j]=0;
			tr[i].end=0;
		}
	}
	return 0;
}
