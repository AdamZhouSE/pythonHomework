
#include<bits/stdc++.h>
using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
#define ls i<<1
#define rs ls | 1
#define pii pair<int,int>
#define MP make_pair
typedef long long LL;
typedef unsigned long long ULL;
const long long INF = 1e18+1LL;
const double pi = acos(-1.0);
const int N = 2e4+10, M = 1e3+20,inf = 2e9;

int *ran,r[N],sa[N],height[N],wa[N],wb[N],wm[N];
bool cmp(int *r,int a,int b,int l) {
    return r[a] == r[b] && r[a+l] == r[b+l];
}
void SA(int *r,int *sa,int n,int m) {
    int *x=wa,*y=wb,*t;
    for(int i=0;i<m;++i)wm[i]=0;
    for(int i=0;i<n;++i)wm[x[i]=r[i]]++;
    for(int i=1;i<m;++i)wm[i]+=wm[i-1];
    for(int i=n-1;i>=0;--i)sa[--wm[x[i]]]=i;
    for(int i=0,j=1,p=0;p<n;j=j*2,m=p){
        for(p=0,i=n-j;i<n;++i)y[p++]=i;
        for(i=0;i<n;++i)if(sa[i]>=j)y[p++]=sa[i]-j;
        for(i=0;i<m;++i)wm[i]=0;
        for(i=0;i<n;++i)wm[x[y[i]]]++;
        for(i=1;i<m;++i)wm[i]+=wm[i-1];
        for(i=n-1;i>=0;--i)sa[--wm[x[y[i]]]]=y[i];
        for(t=x,x=y,y=t,i=p=1,x[sa[0]]=0;i<n;++i) {
            x[sa[i]]=cmp(y,sa[i],sa[i-1],j)?p-1:p++;
        }
    }
    ran=x;
}
void Height(int *r,int *sa,int n) {
    for(int i=0,j=0,k=0;i<n;height[ran[i++]]=k)
    for(k?--k:0,j=sa[ran[i]-1];r[i+k] == r[j+k];++k);
}

const ULL mod = 10000019ULL;
int n,m;
ULL sqr[300],has[120][120];
char a[210][120];
map<ULL,int >mp;
int main() {
    sqr[0] = 1;
    for(int i = 1; i <= 200; ++i) sqr[i] = sqr[i-1] * mod;
    scanf("%d%d",&n,&m);
    for(int i = 1; i <= n; ++i) {
        scanf("%s",a[i]+1);
        has[i][0] = 0;
        for(int j = 1; j <= m; ++j) {
            has[i][j] = has[i][j-1] * mod + a[i][j] - 'A' + 1;
        }
    }
    LL ans = 0;
    for(int y = 1; y <= m; ++y) {
        int cnt = 0,san = 1;
        mp.clear();
        for(int j = 1; j + y - 1 <= m; ++j) {
             for(int i = 1; i <= n; ++i){
                int l = j, rr = j + y - 1;
                ULL now = has[i][rr] - has[i][l-1]*sqr[y];
                if(mp[now] == 0) mp[now] = san++;
                r[cnt++] = mp[now];
            }
            r[cnt++] = san++;
        }
        r[cnt] = 0;

        SA(r,sa,cnt+1,san);
        Height(r,sa,cnt);
        //for(int i = 0; i <= cnt; ++i) cout<<sa[i]<<" "<<ran[i]<<" "<<height[i]<<endl;
       // return 0;
        ans += n*(n+1)/2*(m-y+1);

        for(int i = 1; i <= cnt; ++i) {
            ans -= height[i];
        }
    }
    printf("%lld\n",ans);
    return 0;
}