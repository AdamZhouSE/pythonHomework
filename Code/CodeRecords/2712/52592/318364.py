#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#define mem(x,v) memset(x,v,sizeof(x)) 
#define go(i,a,b)  for (int i = a; i <= b; i++)
#define og(i,a,b)  for (int i = a; i >= b; i--)
using namespace std;
typedef long long LL;
const double EPS = 1e-10;
const int INF = 0x3f3f3f3f;
const int N = 2e4+10;
struct Tree{
	int fail;
	int vis[27];
	int num;
	string t;
}Ac[N];
struct node{
	string s;
	int id;
	bool operator <(const node &a)const{
		return id < a.id;
	}
}p[200];
int ans,cnt,cur[N],tt,tot;
bool vis[N];
 
void Clean(int x){
	mem(Ac[x].vis,0);
	Ac[x].fail = 0;
	Ac[x].num = 0;
	cur[x] = 0;
}
 
void Build(int id, string s){
	int len = s.length();
	int now = 0;
	go(i,0,len-1){
		if(Ac[now].vis[s[i]-'a'] == 0) Ac[now].vis[s[i]-'a'] = ++ cnt,Clean(cnt);
		now = Ac[now].vis[s[i]-'a'];
	}
	Ac[now].num = id;
	Ac[now].t = s;
}
 
void Get_Fail(){
	queue<int>Q; while(!Q.empty()) Q.pop();
	go(i,0,25) {
		if (Ac[0].vis[i]!=0) {
			Ac[Ac[0].vis[i]].fail = 0;
			Q.push(Ac[0].vis[i]);
		}
	}
	while(!Q.empty()){
		int u = Q.front(); Q.pop();
		go(i,0,25){
			if (Ac[u].vis[i]){
				Ac[Ac[u].vis[i]].fail = Ac[Ac[u].fail].vis[i];
				Q.push(Ac[u].vis[i]);
			} else 
			Ac[u].vis[i] = Ac[Ac[u].fail].vis[i];
		}
	}
 
}
void init(int n){
	string s;
	ans = cnt = 0;
	Clean(0);
	go(i,1,n) {
		cin>>s;
		Build(i,s);
	}
}
void Ac_Query(string s){
	int len = s.length(); 
	int now = 0;
	go(i,0,len-1){
		now = Ac[now].vis[s[i]-'a'];
		for(int t = now; t; t = Ac[t].fail){
			if (Ac[t].num > 0) {
				cur[t]++;
			if (cur[t] > ans){
				ans = cur[t];
				tt = 0;
				p[tt].id = Ac[t].num;
				p[tt].s = Ac[t].t;
 
			} else
			if (cur[t] == ans){
				tt++;
				p[tt].id = Ac[t].num;
				p[tt].s = Ac[t].t;
			}
		}
		}
	}
}
int main(){
	int n;
	while(~scanf("%d",&n) && n){
		string s;
		init(n);
		Get_Fail();
		cin>>s;
		Ac_Query(s);
		sort(p,p+tt+1);
		printf("%d\n",ans);
		go(i,0,tt)
		cout<<p[i].s<<endl;
	}
 
 
	return 0;
}
