#include <cstdio>
#include <cstring>
using namespace std;
typedef long long ll;
const int N=1005;
const int MOD=1e9+7;
int n,m,blacksum;
ll kk;
char str[N][N];
int map[N][N];
int hcnt,vcnt,lh,lv;
inline void plus(int &x,int y){
    x=(x+y>=MOD)?(x+y-MOD):x+y;
}
inline void swap(int &x,int &y){
    x^=y^=x^=y;
}
inline int fmi(int x,ll y){
    int res=1;
    for(;y;x=1LL*x*x%MOD,y>>=1)
        if(y&1)
            res=1LL*res*x%MOD;
    return res;
}
struct Mat{/*{{{*/
    int n,m;
    int a[4][4];
    Mat(){
        memset(a,0,sizeof a);   
    }
    Mat(int _n,int _m){
        n=_n; m=_m;
        clear();
    }
    void setUnit(){
        if(n!=m) return;
        for(int i=1;i<=n;i++)
            a[i][i]=1;
    }
    void clear(){
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                a[i][j]=0;
    }
    friend Mat operator * (Mat u,Mat v){
        Mat res=Mat(u.n,v.m);
        for(int i=1;i<=u.n;i++)
            for(int j=1;j<=v.m;j++)
                for(int k=1;k<=u.m;k++)
                    //(res.a[i][j]+=1LL*u.a[i][k]*v.a[k][j]%MOD)%=MOD;
                    plus(res.a[i][j],1LL*u.a[i][k]*v.a[k][j]%MOD);
        return res;
    }
}O,T;/*}}}*/
void readData(){
    scanf("%d%d%lld",&n,&m,&kk);
    for(int i=1;i<=n;i++){
        scanf("%s",str[i]+1);
        for(int j=1;j<=m;j++)
            blacksum+=(str[i][j]=='#');
    }
}
int getTypeAndInit(){
    for(int i=1;i<=n;i++)
        hcnt+=(str[i][1]=='#'&&str[i][m]=='#');
    for(int j=1;j<=m;j++)
        vcnt+=(str[1][j]=='#'&&str[n][j]=='#');
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++){
            if(j<m)
                lh+=(str[i][j]=='#'&&str[i][j+1]=='#');
            if(i<n)
                lv+=(str[i][j]=='#'&&str[i+1][j]=='#');
        }
    if(hcnt&&vcnt) return 1;
    else if(!hcnt&&!vcnt) return 2;
    if(hcnt){
        swap(hcnt,vcnt);
        swap(lh,lv);
    }
    return 3;
}
void fillMatrix(){
    O=Mat(1,3);
    O.a[1][1]=blacksum; O.a[1][2]=lv; O.a[1][3]=vcnt;
    T=Mat(3,3);
    T.a[1][1]=blacksum;
    T.a[2][2]=blacksum; T.a[3][2]=lv;
    T.a[3][3]=vcnt;
}
Mat mat_fmi(Mat x,ll y){
    Mat res=Mat(x.n,x.n);
    res.setUnit();
    for(;y;x=x*x,y>>=1)
        if(y&1)
            res=res*x;
    return res;
}
void solve(){
    fillMatrix();
    T=mat_fmi(T,kk-2);
    O=O*T;
    int ans=O.a[1][1]-O.a[1][2];
    printf("%d\n",ans<0?ans+MOD:ans);
}
int main(){
    readData(); 
    if(kk<=1){
        puts("1");
        return 0;
    }
    int type=getTypeAndInit();
    if(type==1)//whole
        puts("1");
    else if(type==2)//isolated
        printf("%d\n",kk==0?1:fmi(blacksum,kk-1));
    else
        solve();
    return 0;
}