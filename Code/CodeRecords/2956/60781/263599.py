#include<cstdio>
#include<cstring>
#include<algorithm>
#define P 1000000007
#define ll long long
using namespace std;
ll n;
char S[100005];
int add(int x,int y)  {return x+y>=P?x+y-P:x+y;}
int dec(int x,int y)  {return x-y< 0?x-y+P:x-y;}
int mul(int x,int y)  {return 1ll*x*y%P;}
struct matrix{
	int m[26][26];
	matrix(int t=0){
		memset(m,0,sizeof(m));
		for(int i=0;i<26;++i)  m[i][i]=t;
	}
	friend matrix operator*(const matrix &A,const matrix &B){
		matrix C(0);
		for(int i=0;i<26;++i)
			for(int k=0;k<26;++k)
				for(int j=0;j<26;++j)
					C.m[i][j]=add(C.m[i][j],mul(A.m[i][k],B.m[k][j]));
		return C;
	}
	friend matrix operator^(matrix A,ll B){
		matrix ans(1);
		for(;B;B>>=1,A=A*A)  if(B&1)  ans=ans*A;
		return ans;
	}
}A,B;
int main(){
	scanf("%lld%s",&n,S+1);
	int len=strlen(S+1),ans=0;
	for(int i=0;i<26;++i)  A.m[0][i]=1;
	for(int i=0;i<26;++i)  for(int j=0;j<26;++j)  B.m[i][j]=1;
	for(int i=1;i<len;++i)  B.m[S[i]-'a'][S[i+1]-'a']=0;
	A=A*(B^(n-1));
	for(int i=0;i<26;++i)  ans=add(ans,A.m[0][i]);
	printf("%d\n",ans);
	return 0;
}
