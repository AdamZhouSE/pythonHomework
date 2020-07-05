#include<bits/stdc++.h>
#define re register
using namespace std;
const int N=3e5+5;
const int mod=1e9+7;
long long n;
char s[N];
struct mat{
	int a[30][30];
	inline const int *const operator[](const int &offset)const{return a[offset];}
	inline int *const operator[](const int &offset){return a[offset];}
	friend inline mat operator*(const mat&a,const mat&b){
		mat c;memset(c.a,0,sizeof(c.a));
		for(int re i=0;i^26;++i)
			for(int re j=0;j^26;++j)
				for(int re k=0;k^26;++k)
					if((c[i][j]+=1ll*a[i][k]*b[k][j]%mod)>=mod)
						c[i][j]-=mod;
		return c;
	}
}a,b;
int main(){
	scanf("%lld",&n);scanf("%s",s);
	for(int re i=0;i^26;i++)
		for(int re j=0;j^26;j++)
			a[i][j]=1;
	for(int re i=0;i^26;++i)b[i][i]=1;
	int len=strlen(s)-1;
	for(int re i=0;i^len;i++)a[s[i]-'a'][s[i+1]-'a']=0;
	--n;
	while(n){if(n&1)b=b*a;a=a*a;n>>=1;}
	int ans=0;
	for(int re i=0;i^26;++i)
		for(int re j=0;j^26;++j)
			(ans+=b[i][j])%=mod;
	cout<<ans<<"\n";
}
