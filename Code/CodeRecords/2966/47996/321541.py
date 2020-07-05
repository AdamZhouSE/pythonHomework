#include<bits/stdc++.h>
#define ull unsigned long long
#define re register
#define cs const

cs int N=1e6+10,oo=1e9+7;
cs ull base=131;

struct node{
	int l,r;
	node(int _l=0,int _r=0){l=_l,r=_r;}
}ans[3];
int Case,n,m,s[N],t[N];bool ok[N];
int nxt_s[N],nxt_t[N];
ull hash_s[N],hash_t[N],Pow[N];

namespace IO{
	cs int Rlen=1<<22|1;
	char buf[Rlen],*p1,*p2;
	inline char gc(){return (p1==p2)&&(p2=(p1=buf)+fread(buf,1,Rlen,stdin),p1==p2)?EOF:*p1++;}
	template<typename T>
	inline T get(){
		char ch=gc();T x=0;
		while(!isdigit(ch)) ch=gc();
		while(isdigit(ch)) x=((x+(x<<2))<<1)+(ch^48),ch=gc();
		return x;
	}
	inline int gi(){return get<int>();}
}
using IO::gi;
inline void Min(int &x,int y){if(x>y)x=y;}
inline void Max(int &x,int y){if(x<y)x=y;}
inline int min(int x,int y){return x<y?x:y;}
inline int max(int x,int y){return x>y?x:y;}

inline int collect(ull *a,int l,int r){return a[r]-a[l-1]*Pow[r-l+1];}
inline int comp(ull *a,int l,ull *b,int x,int len){return collect(a,l,l+len-1)==collect(b,x,x+len-1);}

inline void get_nxt(int *S,int *nxt){
	int j=0;nxt[1]=0;
	for(int re i=2;i<=n;++i){
		while(j&&S[i]!=S[j+1]) j=nxt[j];
		nxt[i]=(j+=(S[i]==S[j+1]));
	}
}
inline bool checkABC(){
	if(hash_s[n]==hash_t[n]){
		ans[0]=node(1,1),ans[1]=node(2,2),ans[2]=node(3,n);
		return true;
	}return false;
}

inline bool checkACB(){
	ok[0]=true;
	for(int re i=1;i<=n;++i) ok[i]=(s[i]==t[i])&&ok[i-1];
	for(int re i=n,pos_s=n+1,pos_t=n+1;i>=1;--i){
		while(pos_s!=n+1&&s[pos_s-1]!=t[i]) pos_s=n+1-nxt_s[n+1-pos_s];
		pos_s-=(s[pos_s-1]==t[i]);
		while(pos_t!=n+1&&t[pos_t-1]!=s[i]) pos_t=n+1-nxt_t[n+1-pos_t];
		pos_t-=(t[pos_t-1]==s[i]);
		if(!ok[i-1]) continue;
		int len_s=n-pos_s+1,len_t=n-pos_t+1;
		if(collect(hash_s,i,n-len_s)==collect(hash_t,i+len_s,n)){
			ans[0]=node(1,i-1),ans[1]=node(i+len_s,n),ans[2]=node(i,i+len_s-1);
			return true;
		}
		if(collect(hash_t,i,n-len_t)==collect(hash_s,i+len_t,n)){
			ans[0]=node(1,i-1),ans[1]=node(n-len_t+1,n),ans[2]=node(i,n-len_t);
			return true;
		}
	}return false;
}

inline bool checkBAC(){
	ok[n+1]=true;
	for(int re i=n;i>=1;--i) ok[i]=(s[i]==t[i])&&ok[i+1];
	for(int re i=1,pos_s=0,pos_t=0;i<=n;++i){
		while(pos_s&&s[pos_s+1]!=t[i]) pos_s=nxt_s[pos_s];
		pos_s+=(s[pos_s+1]==t[i]);
		while(pos_t&&t[pos_t+1]!=s[i]) pos_t=nxt_t[pos_t];
		pos_t+=(t[pos_t+1]==s[i]);
		if(!ok[i+1]) continue;
		if(comp(hash_t,1,hash_s,pos_s+1,i-pos_s)){
			ans[0]=node(i-pos_s+1,i),ans[1]=node(1,i-pos_s),ans[2]=node(i+1,n);
			return true;
		}
		if(comp(hash_s,1,hash_t,pos_t+1,i-pos_t)){
			ans[0]=node(pos_t+1,i),ans[1]=node(1,pos_t),ans[2]=node(i+1,n);
			return true;
		}
	}return false;
}

inline bool checkBCA(){
	for(int re len=1;len<=n-2;++len){
		if(
			collect(hash_s,1,len)==collect(hash_t,n-len+1,n) and
			collect(hash_s,len+1,n)==collect(hash_t,1,n-len)
		){ans[0]=node(n-len+1,n),ans[1]=node(1,1),ans[2]=node(2,n-len);return true;}
	}return false;
}

inline bool checkCAB(){
	for(int re len=1;len<=n-2;++len){
		if(
			collect(hash_s,n-len+1,n)==collect(hash_t,1,len) and
			collect(hash_s,1,n-len)==collect(hash_t,len+1,n)
		){ans[0]=node(len+1,len+1),ans[1]=node(len+2,n),ans[2]=node(1,len);return true;}
	}return false;
}

int st[N<<2],top,S[N<<2],R[N<<2],rpos[N<<2];bool vis[N<<2];
int q[N<<2],qn;
inline void manacher(int *S,int *R,int up){
	int pos=0,mx=0;
	for(int re i=0;i<=up;++i){
		R[i]=(mx>i)?(min(R[(pos<<1)-i],mx-i)):1;
		while(i-R[i]>=0&&(S[i-R[i]]==S[i+R[i]])) ++R[i];
		if(mx<i+R[i]) mx=i+R[i],pos=i;
		Max(rpos[i-R[i]+1],i+R[i]-1);
		if(i+R[i]-1==top) vis[i-R[i]+1]=true;
	}
}

//双偶回文 
inline bool check(int l,int r){return l<r&&((r-l)%4==0);}

//端点为-1 
inline bool is_p(int l,int r){
	if(l>r) return false;
	int mid=(l+r)>>1;
	return (mid-R[mid]+1<=l);
}

inline bool checkCBA(){
	top=0,qn=0;
	for(int re i=1;i<=n;++i) st[++top]=s[i],st[++top]=t[n+1-i];
	for(int re i=1;i<=top;++i) S[(i-1)<<1]=-1,S[(i-1)<<1|1]=st[i];
	S[top<<=1]=-1;
	for(int re i=0;i<=top;i+=2) rpos[i]=0,vis[i]=false;
	manacher(S,R,top);
	for(int re i=2;i<=top;i+=2){
		Max(rpos[i],rpos[i-2]-2);
		if(vis[i]) q[++qn]=i;
	}
//		rpos[i]:i向右最长回文串的右端点
	int head=1;
	for(int re i=4;i<=top;i+=4) if(is_p(0,i)){
		while(q[head]<i) ++head;
		if(check(i,rpos[i])){
			if(check(rpos[i],top)&&is_p(rpos[i],top)){
				int lenA=i/4,lenC=(top-rpos[i])/4;
				ans[0]=node(n-lenA+1,n),ans[1]=node(lenC+1,n-lenA),ans[2]=node(1,lenC);
				return true;
			}
		}
		if(check(q[head],top)){
			if(check(i,q[head])&&is_p(i,q[head])){
				int lenA=i/4,lenC=(top-q[head])/4;
				ans[0]=node(n-lenA+1,n),ans[1]=node(lenC+1,n-lenA),ans[2]=node(1,lenC);
				return true;
			}
		}
	}return false;
}
inline void print(){
	puts("YES");
	printf("%d %d\n",ans[0].l,ans[0].r);
	printf("%d %d\n",ans[1].l,ans[1].r);
	printf("%d %d\n",ans[2].l,ans[2].r);
}
int main(){
	Case=gi(),Pow[0]=1;
	for(int re i=1;i<N;++i) Pow[i]=Pow[i-1]*base;
	while(Case--){
		n=gi(),m=gi();
		for(int re i=1;i<=n;++i) s[i]=gi(),hash_s[i]=hash_s[i-1]*base+s[i];
		for(int re i=1;i<=n;++i) t[i]=gi(),hash_t[i]=hash_t[i-1]*base+t[i];
		get_nxt(s,nxt_s),get_nxt(t,nxt_t);
		if(checkABC()) print();
		else if(checkBCA()) print();
		else if(checkCAB()) print();
		else if(checkACB()) print();
		else if(checkBAC()) print();
		else if(checkCBA()) print();
		else puts("NO");
	}
}
