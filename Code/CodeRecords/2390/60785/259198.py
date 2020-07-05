#include <cstdio>
#include <cctype>
#define rr register
using namespace std;
int a[4096],er[13],n; long long jc[13],ans;
inline signed iut(){
    rr int ans=0; rr char c=getchar();
    while (!isdigit(c)) c=getchar();
    while (isdigit(c)) ans=(ans<<3)+(ans<<1)+(c^48),c=getchar();
    return ans;
}
inline bool check(int st,int m){
    for (rr int i=st+1;i<st+er[m];++i)
        if (a[i-1]+1!=a[i]) return 0;
    return 1;
}
inline void Swap(int &a,int &b){a^=b,b^=a,a^=b;}
inline void Twap(int l1,int l2,int m){for (rr int i=0;i<er[m];++i) Swap(a[l1+i],a[l2+i]);}
inline void dfs(int dep,int now){
    if (dep>n) {ans+=jc[now]; return;}
    rr int pos1=-1,pos2=-1;
    for (rr int i=0;i<er[n];i+=er[dep])
    if (!check(i,dep)){
        if (pos2==-1) pos2=pos1,pos1=i;
            else return;
    }
    if (pos1==-1&&pos2==-1) dfs(dep+1,now);
    else if (pos2==-1){
        Twap(pos1,pos1+er[dep-1],dep-1);
        if (check(pos1,dep)) dfs(dep+1,now+1);
        Twap(pos1,pos1+er[dep-1],dep-1);
    }else{
        for (rr int k1=0,flag=0;k1<2;++k1)
        for (rr int k2=0;k2<2;++k2){
            Twap(pos1+k1*er[dep-1],pos2+k2*er[dep-1],dep-1);
            if (check(pos1,dep)&&check(pos2,dep)) dfs(dep+1,now+1),flag=1;
            Twap(pos1+k1*er[dep-1],pos2+k2*er[dep-1],dep-1);
            if (flag) {flag=0; break;}
        }
    }
}
signed main(){
    n=iut(),er[0]=jc[0]=1;
    for (rr int i=1;i<=n;++i)
        er[i]=er[i-1]<<1,jc[i]=jc[i-1]*i;
    for (rr int i=0;i<er[n];++i) a[i]=iut();
    dfs(1,0);
    return !printf("%lld",ans);
}