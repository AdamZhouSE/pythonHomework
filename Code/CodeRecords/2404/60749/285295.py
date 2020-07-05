#include <cstdio>

using namespace std;

int n,s,ans;
int a[100005];
int ls[100005],ne[200005],y[200005];
long long b[100005];

bool find(int r,long long k){
    int l=0,ss=0;
    while (l<=r){
        int mid=(l+r)/2;
        if (b[mid]<=k) ss=mid,l=mid+1;
                  else r=mid-1;
    }
    if (b[ss]==k) return true;
    return false;
}

void dfs(int x,int k){
    b[k]=b[k-1]+a[x];
    if (find(k,b[k]-s)) ans++;
    for (int i=ls[x];i;i=ne[i])
    {
        dfs(y[i],k+1);
    }
    b[k]=0;
}

int main(){
    scanf("%d%d",&n,&s);
    for (int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    for (int i=1;i<n;i++){
        int x,to;
        scanf("%d%d",&x,&to);
        ne[i]=ls[x];ls[x]=i;y[i]=to;
    }
    b[0]=0;
    dfs(1,1);
    printf("%d\n",ans);
    return 0; 
}
