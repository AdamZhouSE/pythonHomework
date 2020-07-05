#include<bits/stdc++.h>
#define reg register int
#define il inline
#define numb (ch^'0')
using namespace std;
typedef long long ll;
il void rd(int &x){
    char ch;x=0;bool fl=false;
    while(!isdigit(ch=getchar()))(ch=='-')&&(fl=true);
    for(x=numb;isdigit(ch=getchar());x=x*10+numb);
    (fl==true)&&(x=-x);
}
namespace Miracle{
const int N=200000+5;
const int inf=0x3f3f3f3f;
int n,m;
int l1,l2;
char s1[N],s2[N],s[2*N];
int x[4*N],y[4*N],rk[2*N],sa[2*N];
int c[2333],num;
int hei[2*N];
void getsa(){
    m=233;
    for(reg i=1;i<=n;++i) ++c[x[i]=s[i]];
    //for(reg i=1;i<=n;++i) cout<<x[i]<<" ";cout<<endl;
    for(reg i=2;i<=m;++i) c[i]+=c[i-1];
    for(reg i=1;i<=n;++i) sa[c[x[i]]--]=i;
    //for(reg i=1;i<=n;++i) cout<<sa[i]<<" ";cout<<endl;
    for(reg k=1;k<=n;k<<=1){
        num=0;
        for(reg i=n-k+1;i<=n;++i) y[++num]=i;
        for(reg i=1;i<=n;++i) if(sa[i]>k) y[++num]=sa[i]-k;
        for(reg i=1;i<=m;++i) c[i]=0;
        for(reg i=1;i<=n;++i) ++c[x[i]];
        for(reg i=2;i<=m;++i) c[i]+=c[i-1];
        for(reg i=n;i>=1;--i) sa[c[x[y[i]]]--]=y[i],y[i]=0;
        swap(x,y);
        num=1;x[sa[1]]=1;
        for(reg i=2;i<=n;++i){
            x[sa[i]]=(y[sa[i]]==y[sa[i-1]])&&(y[sa[i]+k]==y[sa[i-1]+k])?num:++num;
        }
        if(num==n) break;
        m=num;
        
    } 
}
void gethei(){
    int k=0;
    for(reg i=1;i<=n;++i) rk[sa[i]]=i;
    for(reg i=1;i<=n;++i){
        if(rk[i]==1) continue;
        if(k) --k;
        int j=sa[rk[i]-1];
        while(j+k<=n&&i+k<=n&&s[i+k]==s[j+k]) ++k;
        hei[rk[i]]=k;
    }
}
ll ans;
int be[2*N];
void divi(int l,int r){
//    cout<<" divi "<<l<<" and "<<r<<"-------------------------------"<<endl;
    if(l==r) return ;
    int mid=(l+r)>>1;
//    cout<<" mid "<<mid<<endl;
    int cnt1=0,cnt2=0;
    int mir=inf,mil=inf;
    int ptr=mid+1;
    for(reg i=mid+1;i<=r;++i){
        mir=min(mir,hei[i]);
        while(ptr-1>=l&&hei[ptr]>=mir) {
            if(be[ptr-1]==1) ++cnt1;
            else if(be[ptr-1]==2) ++cnt2;
            ptr--;
        }
        if(be[i]==1) ans+=(ll)cnt2*mir;
        else if(be[i]==2) ans+=(ll)cnt1*mir;
    }
    cnt1=0,cnt2=0;
    ptr=mid+1;
    for(reg i=mid;i>=l;--i){
        mil=min(mil,hei[i+1]);
        while(ptr<=r&&hei[ptr]>mil){
            if(be[ptr]==1) ++cnt1;
            else if(be[ptr]==2) ++cnt2;
            ptr++;
        }
        if(be[i]==1) ans+=(ll)cnt2*mil;
        else if(be[i]==2) ans+=(ll)cnt1*mil;
    }
    divi(l,mid);
    divi(mid+1,r);
}
int main(){
    scanf("%s%s",s1+1,s2+1);
    l1=strlen(s1+1);l2=strlen(s2+1);
    n=l1+l2+1;
    for(reg i=1;i<=l1;++i) s[i]=s1[i];
    s[l1+1]='#';
    for(reg i=1;i<=l2;++i) s[l1+1+i]=s2[i];
    
//    cout<<n<<" : "<<s+1<<endl;
    
    getsa();gethei();
    
    for(reg i=1;i<=l1;++i) be[rk[i]]=1;
    be[rk[l1+1]]=3;
    for(reg i=1;i<=l2;++i) be[rk[l1+1+i]]=2;
    
//    for(reg i=1;i<=n;++i){
//        cout<<hei[i]<<" ";
//    }cout<<endl;
//    for(reg i=1;i<=n;++i){
//        cout<<be[i]<<" ";
//    }cout<<endl;
//    
    
    divi(1,n);
    printf("%lld",ans);
    return 0;
}

}
int main(){
    Miracle::main();
    return 0;
}