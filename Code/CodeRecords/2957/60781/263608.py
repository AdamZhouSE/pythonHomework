#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>
#define LL long long
using namespace std;
inline int read(){
    int X=0,w=0; char c=0;
    while(c<'0'||c>'9') {w|=c=='-';c=getchar();}
    while(c>='0'&&c<='9') X=(X<<3)+(X<<1)+(c^48),c=getchar();
    return w?-X:X;
}
void fff(){
    freopen("strange.in","r",stdin);
    freopen("strange.out","w",stdout);
}
char s[200100],k1,k2;
int n,c1,c2;
struct node{
    int k1,k2,c1,c2;
}d[200100];
map<pair<int,int>,int> b[30];
int a[27];
int main(){
//  fff();
    scanf("%s",s+1);
    n=strlen(s+1);
    int pos=0,cnt=0;
    s[0]=s[1];
    for (int i=1;i<=n;i++){
        while (pos<n){
            if(s[pos]!=s[pos+1]&&cnt==1) break;
            if(s[pos]!=s[pos+1]){
                cnt++;
                k2=s[pos+1];c2++;
            }else if(c2) c2++;else k1=s[pos],c1++;
            pos++;
        }
        d[i]=(node){k1-'a'+1,k2-'a'+1,c1,c2};
        a[k1-'a'+1]=max(c1,a[k1-'a'+1]);
        if(s[i]!=s[i+1]){
            cnt--;
            k1=k2;
            c1=c2;
            c2=0;
        }else c1--;
    }
    LL ans=0;
    for (int i=1;i<=26;i++)ans+=a[i];
    for (int i=1;i<=n;i++){
        if(d[i].c2==0) continue;
        int tmp=b[d[i].k1][make_pair(d[i].c1,d[i].k2)];
        b[d[i].k1][make_pair(d[i].c1,d[i].k2)]=max(tmp,d[i].c2);
        ans+=max(0,d[i].c2-tmp);
    }
    printf("%lld\n",ans);
}
