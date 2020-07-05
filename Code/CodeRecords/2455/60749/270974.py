
#include<iostream>

#include<cstdio>

#include<cstring>

#include<cmath>

#include<algorithm>

#include<string>

#include<cstdlib>

#include<queue>

#include<set>

#include<map>

#include<stack>

#include<ctime>

#include<vector>

#define INF 0x3f3f3f3f

#define PI acos(-1.0)

#define N 100000

#define MOD 16007

#define E 1e-6

#define LL long long

using namespace std;

struct Edge{

    int to;

    int next;

}edge[N];

int n;

int a[N];

int head[N],f[N];

int cnt,res;

void addEdge(int x,int y){

    edge[++cnt].to=y;

    edge[cnt].next=head[x];

    head[x]=cnt;

}

void treeDP(int x,int father){

    f[x]=a[x];

    for(int i=head[x];i;i=edge[i].next){

        int y=edge[i].to;

        if(y!=father){

            treeDP(y,x);

            f[x]+=max(0,f[y]);

        }

    }

    res=max(res,f[x]);

}

int main()

{

    scanf("%d",&n);

    for(int i=1;i<=n;i++)

        scanf("%d",&a[i]);

    for(int i=1;i<n;i++){

        int x,y;

        cin>>x>>y;

        addEdge(x,y);

        addEdge(y,x);

    }

    treeDP(1,0);

    printf("%d",res);

 

	return 0;

}
