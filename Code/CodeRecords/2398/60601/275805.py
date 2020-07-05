#include<cstdio>
#include<queue>
#define max(a,b) ((a)>(b)?(a):(b))
#include<vector>
using namespace std;
int n,t;
int a[200005];
int ans;
struct cmp1{
    bool operator ()(int &a,int &b){
        return a>b;
    }
};
priority_queue<int,vector<int>,cmp1>q;
bool check(int num){
    int tmp;
    for(int i=1;i<=num;i++)q.push(a[i]);
    for(int i=num+1;i<=n;i++){
    tmp=q.top();
    q.pop();
    tmp+=a[i];
    if(tmp>t)return false;
    q.push(tmp);    
    }
    tmp=0;
    for(int i=1;i<=num;i++)
    {
        int tt=q.top();
        q.pop();
    }
    return tmp<=t;
}
int main(){
    freopen("dance.in","r",stdin);
    freopen("dance.out","w",stdout);
    scanf("%d%d",&n,&t);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]);
    int l=1,r=n;
    ans=n;
    while(l<=r){
        int mid=(l+r)>>1;
        if(check(mid))r=mid-1,ans=mid;
        else l=mid+1;
    }
    printf("%d\n",ans);
    fclose(stdin);
    fclose(stdout);
}