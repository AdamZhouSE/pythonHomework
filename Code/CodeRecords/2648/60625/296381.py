#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<queue>
#define maxn 1000005
using namespace std;
typedef long long ll;
const int p = 13331, q = 998244353;
int read() {
	int x = 0, f = 1, ch = getchar();
	while(!isdigit(ch)) {if(ch == '-') f = -1; ch = getchar();}
	while(isdigit(ch)) x = (x << 1) + (x << 3) + ch - '0', ch = getchar();
	return x * f;
}
 
char s[maxn], t[maxn], stc[maxn];
int top = 0;
ll hash[maxn], T;
ll power(ll a, ll b) {//这里是个快速幂 
	ll ans = 1;
	while(b) {
		if(b & 1) ans = ans * a % q;
		b >>= 1, a = a * a % q;
	}
	return ans;
}
 
signed main() {
	scanf("%s%s", s + 1, t + 1);
	int lens = strlen(s + 1), lent = strlen(t + 1);
	for(int i = 1; i <= lent; i++) T = (T * p + t[i] - 'a') % q;//预处理出t的hash值 
	
	for(int i = 1; i <= lens; i++) {
		stc[++top] = s[i];//往stack里扔字符 
		hash[top] = (hash[top - 1] * p + s[i] - 'a') % q;//处理出以当前字符结尾的hash值 
		if(top >= lent && (hash[top] - hash[top - lent] * power(p, lent) % q + q) % q == T) //如果出现了t，匹配上了 
			for(int j = 1; j <= lent; j++) top--;//那就top--，pop出去 
	}
	
	for(int i = 1; i <= top; i++) printf("%c", stc[i]);
	return 0;
}
/*
whatthemomooofun
moo
*/