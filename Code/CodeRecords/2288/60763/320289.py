#include<cstdio>
int main(){
    long long int n,m;
    while(scanf("%lld%lld",&m,&n)!=EOF){
    if(n==0 && m==0) break;
    int ans;
    int cnt=1;
    if(n>=m) ans = 1;
    else ans = 0;
    long long int l=m,r=m;
    while(2*r+1<=n){
        cnt*=2;
        l=2*l;
        r=2*r+1;
        ans += cnt;
    }
    l=2*l;
    r=2*r+1;
    while(l<=n && l<=r){
        l++;
        ans++;
    }
    printf("%d\n",ans);
}
     
     
     
    return 0;
}