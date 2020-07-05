#include<iostream>
#include<cstdio>
#include<cstring>
#define p 1000003
#define int long long
using namespace std;
int f[64][64];
int ywy=1;
int hsh[1000005];
unsigned char bv[64][64];
int dp(int len,int bit){//记搜实现的数位dp
    if(len==0)return(0);
    if(bv[len][bit])return(f[len][bit]);
    bv[len][bit]=1;
    if((ywy<<len)<=(ywy<<bit))return(f[len][bit]=0);
    if((ywy<<len)==(ywy<<(bit+1)))return(f[len][bit]=(ywy<<bit));
    return(f[len][bit]=dp(len-1,bit)<<1);
}
int getnum(int num,int bit){//递归n的每一位
    if(num==0)return(0);
    if(num<(ywy<<bit))return(0);
    if(num>=(ywy<<bit)&&num<(ywy<<(bit+1)))return(num-(ywy<<bit)+1);
    int tmp=num;
    while(tmp!=(tmp&-tmp))tmp-=(tmp&-tmp);
    int bitof=hsh[tmp%p];
    //printf("dp(%d,%d)=%d\n",bitof-1,bit,dp(bitof-1,bit));
    return(dp(bitof,bit)+getnum(num-tmp,bit));
}
signed main(){
    int n;cin>>n;int ans=0;
    for(register int i=0;i<=62;i++){
        hsh[(ywy<<i)%p]=i;//这里用了个小技巧，为了快速取到最高位对应的位数，我直接用哈希记录
    }
    for(register int i=0;i<=62;i++){
        int cjr=getnum(n,i);
        if(cjr&1)ans+=(ywy<<i);//为奇数就把这位加入答案
    }cout<<ans<<endl;
    return(0);
}