#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define Rep(i,v) rep(i,0,(int)v.size()-1)
#define lint long long
#define mod 1000000007
#define ull unsigned lint
#define db long double
#define pb push_back
#define mp make_pair
#define fir first
#define sec second
#define debug(x) cerr<<#x<<"="<<x
#define sp <<" "
#define ln <<endl
using namespace std;
typedef pair<int,int> pii;
typedef set<int>::iterator sit;
namespace INPUT_SPACE{
	const int BS=(1<<24)+5;char Buffer[BS],*HD,*TL;inline int gc() { if(HD==TL) TL=(HD=Buffer)+fread(Buffer,1,BS,stdin);return (HD==TL)?EOF:*HD++; }
	inline int instr(char *s) { int n=0,ch;while((ch=gc())<'a'||ch>'z');s[++n]=char(ch);while((ch=gc())>='a'&&ch<='z') s[++n]=char(ch);return n; }
}using INPUT_SPACE::instr;
namespace OUTPUT_SPACE{
	char ss[500000*15],tt[20];int ssl,ttl;inline int Flush() { return fwrite(ss+1,sizeof(char),ssl,stdout),ssl=0,0; }
	inline int print(int x) { if(!x) ss[++ssl]='0';for(ttl=0;x;x/=10) tt[++ttl]=char(x%10+'0');for(;ttl;ttl--) ss[++ssl]=tt[ttl];return ss[++ssl]='\n'; }
}using OUTPUT_SPACE::print;using OUTPUT_SPACE::Flush;
inline int fast_pow(int x,int k,int ans=1) { for(;k;k>>=1,x=(lint)x*x%mod) (k&1)?ans=(lint)ans*x%mod:0;return ans; }
const int N=500010,LOG=20;int ans[N];
struct SA{
	int n,r,t1[N<<1],t2[N<<1],cnt[N],sa[N],rk[N],h[N],a[N<<1],Log[N],f[N][LOG];
	inline int cmp(int *a,int x,int y,int l) { return a[x]==a[y]&&a[x+l]==a[y+l]; }
	inline int getSA(char *s,int _n,int m,int _r)
	{
		int *x=t1,*y=t2;n=_n,r=_r;
		memset(t1,0,sizeof(int)*(n*2+1));
		memset(t2,0,sizeof(int)*(n*2+1));
		memset(a,0,sizeof(int)*(n*2+1));
		rep(i,1,m) cnt[i]=0;sa[0]=x[0]=a[0]=0;
		rep(i,1,n) cnt[x[i]=a[i]=s[i]-'a'+1]++;
		rep(i,1,m) cnt[i]+=cnt[i-1];
		for(int i=n;i;i--) sa[cnt[x[i]]--]=i;
		for(int j=1,p=0;p<=n;j<<=1,m=p)
		{
			p=0;rep(i,n-j+1,n) y[++p]=i;
			rep(i,1,n) if(sa[i]>j) y[++p]=sa[i]-j;
			rep(i,1,m) cnt[i]=0;
			rep(i,1,n) cnt[x[y[i]]]++;
			rep(i,1,m) cnt[i]+=cnt[i-1];
			for(int i=n;i;i--) sa[cnt[x[y[i]]]--]=y[i];
			swap(x,y);
			rep(i,p=1,n) x[sa[i]]=(cmp(y,sa[i-1],sa[i],j)?p-1:p++);
		}
		rep(i,1,n) rk[sa[i]]=i;
		for(int i=1,j,p=0;i<=n;h[rk[i++]]=p)
			for((p?p--:0),j=sa[rk[i]-1];max(i,j)+p<=n&&a[i+p]==a[j+p];p++);
		rep(i,2,n) f[i][0]=h[i];rep(i,2,n) Log[i]=Log[i>>1]+1;
		for(int j=1;(1<<j)<=n;j++) rep(i,2,n-(1<<j)+1)
			f[i][j]=min(f[i][j-1],f[i+(1<<(j-1))][j-1]);
		return 0;
	}
	inline int operator()(int x,int y)
	{
		if(r) x=n-x+1,y=n-y+1;if(x==y) return n-x+1;
		x=rk[x],y=rk[y];if(x>y) swap(x,y);x++;
		int k=Log[y-x+1];return min(f[x][k],f[y-(1<<k)+1][k]);
	}
}lcp,lcs;
char s[N];
namespace UPDATE_space{
	lint b[N][3];int n;
	inline int update(int L,int R,int a2,int a1,lint a0)
	{
		if(L>R||R>n) return 0;R++;
		lint *bL=b[L],*bR=b[R];
		bL[0]+=a0,bL[1]+=a1,bL[2]+=a2;
		bR[0]-=a0,bR[1]-=a1,bR[2]-=a2;
		return 0;
	}
	inline int getans(int *ans,int n)
	{
		lint v2=0,v1=0,v0=0;
		rep(i,1,n) v2+=b[i][2],v1+=b[i][1],v0+=b[i][0],ans[i]=(ans[i-1]+(lint)i*i*v2+(lint)i*v1+v0)%mod;
		int inv2=fast_pow(2,mod-2);rep(i,1,n) ans[i]=(lint)ans[i]*inv2%mod;return 0;
	}
}using UPDATE_space::update;
inline int solve(int n,int l)
{
	rep(i,2,n/l)
	{
		int p=(i*l+1<=n?lcp((i-1)*l+1,i*l+1):0),s=lcs((i-1)*l,i*l);
		int L=max((i+1)*l-s,i*l),R=min(i*l+p,(i+1)*l-1),k=i*l+p;if(L>R) continue;
		update(L+1,min(R+1,k),1,2*(l-L)+1,(2ll*l-L+1)*(-L));
		update(R+2,k,0,2*(R-L+1),(R-L+1ll)*(2*l-L-R));
	}
	return 0;
}
int main()
{
	int n=instr(s);UPDATE_space::n=n;
	lcp.getSA(s,n,30,0),reverse(s+1,s+n+1);
	lcs.getSA(s,n,30,1),reverse(s+1,s+n+1);
	rep(i,1,n/2) solve(n,i);
	UPDATE_space::getans(ans,n);rep(i,1,n) print(ans[i]);
	return Flush(),0;
}
