#include<bits/stdc++.h>
using namespace std;
const long long mod=1e9+7;
template<long long size>
struct arr{
	long long a[size][size];
	arr(){clear();}
	arr(long long x[size][size]){
		for(long long i=0;i<size;i++)
			for(long long j=0;j<size;j++)
				a[i][j]=x[i][j];
	}
	void clear(){memset(a,0,sizeof a);}
	long long *operator[](long long x){return a[x];}
	friend void print(const arr &x){
		for(long long i=0;i<size;i++,printf("\n"))
			for(long long j=0;j<size;j++)
				printf("%d ",x.a[i][j]);
	}
	friend arr operator*(const arr &x,const arr &y){
		arr c;
		for(long long i=0;i<size;i++)
			for(long long j=0;j<size;j++)
				for(long long k=0;k<size;k++)
					c[i][j]=(c[i][j]+x.a[i][k]*y.a[k][j]%mod)%mod;
		return c;
	}
	friend arr pow(const arr &x,long long k){
		if(k==1) return x;
		arr t=pow(x,k>>1);
		if((k&1)==1) return t*t*x;
		return t*t;
	}
};
arr<26> t,a;
long long n;
long long len;
char str[2000010];
int main(void)
{
	scanf("%lld",&n);
	if(n==1){
		printf("26\n");
		return 0;
	}
	scanf("%s",str);len=strlen(str);
	for(long long i=0;i<26;i++)
		for(long long j=0;j<26;j++)
			t[i][j]=1;
	for(long long i=0;i<26;i++)
		a[i][0]=1;
	for(long long i=1;i<len;i++)
		t[str[i]-'a'][str[i-1]-'a']=0;
	long long ans=0;
	arr<26> tans=pow(t,n-1)*a;
	for(long long i=0;i<26;i++)
		ans=(ans+tans[i][0]%mod)%mod;
	printf("%lld",ans%mod);
    cout << endl;
}
