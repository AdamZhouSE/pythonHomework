#include<cstdio>
using namespace std;
const int N=1e5+10;
int n,m,tot,tr[N][2];
inline int lowbit(int x){
    return x&-x;
}
inline void updata1(int p,int v){
    for(int i=p;i<=n;i+=lowbit(i)) tr[i][0]+=v;  
}
inline int query1(int p){
    int ans=0;
    for(int i=p;i>=1;i-=lowbit(i)) ans+=tr[i][0];   
    return ans;
}
inline void updata2(int p,int v){
    for(int i=p;i<=n;i+=lowbit(i)) tr[i][1]+=v;  
}
inline int query2(int p){
    int ans=0;
    for(int i=p;i>=1;i-=lowbit(i)) ans+=tr[i][1];   
    return ans;
}
int main(){
    scanf("%d%d",&n,&m);
    for(int i=1,x,y,z;i<=m;i++){
        scanf("%d%d%d",&z,&x,&y);
        if(z==1) updata1(x,1),updata2(y,1),tot++;
        else printf("%d\n",tot-(query1(n)-query1(y)+query2(x-1)));
    }
    return 0;
}