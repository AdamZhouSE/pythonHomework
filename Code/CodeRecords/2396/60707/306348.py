#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<math.h>

using namespace std;

const int maxn=100005;

int data[maxn],father[maxn],cnt[maxn],lazy[maxn];
int a[maxn][4];
int son[maxn][4];
int i,j,k,l,n,m,t1,t2,root,x,y;
void qsort(int l,int r){
    int i,j,mid,mid1;
    i=l; j=r; mid=a[(l+r)/2][1]; mid1=a[(l+r)/2][2];
    while (i<=j){
        while ((a[i][1]<mid)||((a[i][1]==mid)&&(a[i][2]<mid1))) i++;
        while ((a[j][1]>mid)||((a[j][1]==mid)&&(a[j][2]>mid1))) j--;
        if (i<=j){
            a[0][1]=a[i][1]; a[i][1]=a[j][1]; a[j][1]=a[0][1];
            a[0][2]=a[i][2]; a[i][2]=a[j][2]; a[j][2]=a[0][2];
            i++;
            j--;
        }
    }
    if (i<r) qsort(i,r);
    if (l<j) qsort(l,j);
}
void pushdown(int x){
    int y;
    if (!lazy[x]) return;
    y=son[x][1]; son[x][1]=son[x][2]; son[x][2]=y;
    if (son[x][1]) lazy[son[x][1]]^=1;
    if (son[x][2]) lazy[son[x][2]]^=1;
    lazy[x]=0;
}

void rotate(int x,int w){
    int y;
    y=father[x];
    cnt[y]=cnt[y]-cnt[x]+cnt[son[x][w]];
    cnt[x]=cnt[x]+cnt[y]-cnt[son[x][w]];
    father[x]=father[y];
    if (father[y]){
        if (son[father[y]][1]==y) son[father[y]][1]=x; else son[father[y]][2]=x;
    }
    son[y][3-w]=son[x][w];
    if (son[x][w]) father[son[x][w]]=y;
    father[y]=x; son[x][w]=y;
}

void splay(int x){
    int y;
    pushdown(x);
    while (father[x]){
        y=father[x];    
        if (!father[y]) pushdown(father[y]);
        pushdown(y);
        pushdown(x);
        if (y==root){
            if (son[y][1]==x) rotate(x,2); else rotate(x,1);
        } else{
            if (y==son[father[y]][1]){
                if (son[y][1]==x) {rotate(y,2); rotate(x,2);} 
                else{rotate(x,1); rotate(x,2);}
            } else{
                if (son[y][1]==x){rotate(x,2); rotate(x,1);} 
                else{rotate(y,1); rotate(x,1);}
            }
        }
    }
    root=x;
}

int kth(int x,int w){
    int i;
    int tmp;
    tmp=x;
    i=root;
    pushdown(i);
    while ((x!=cnt[son[i][w]]+1) && (i)){
        if (x<cnt[son[i][w]]+1) i=son[i][w]; else{
            x=x-cnt[son[i][w]]-1;
            i=son[i][3-w];
        }
        pushdown(i);
    }
    splay(i);
    return i;
}
void dfs(int x){
    if (father[x])
    dfs(father[x]);
    pushdown(x);
}
int findnum(int x){
    int ans;
    //pushdown(x);
    ans=cnt[son[x][1]];
    while (father[x]) {
        //pushdown(father[x]);
        if (son[father[x]][2]==x) ans+=cnt[son[father[x]][1]]+1;
        x=father[x];
    }
    return ans;
}

int main(){
    //freopen("3599.in","r",stdin);
    //freopen("3599.out","w",stdout);
    scanf("%d",&n);
    m=n;
    for (i=2;i<=n+2;i++){
        scanf("%d",&data[i]); 
        father[i]=i-1;
        son[i-1][2]=i;
        cnt[i]=n-i+3;
        a[i-1][1]=data[i];
        a[i-1][2]=i;
    }
    qsort(1,n);
    cnt[1]=n+2;
    root=1;
    for (i=1;i<=m;i++){
        dfs(a[i][2]);
        printf("%d ",findnum(a[i][2]));
        l=kth(findnum(a[i][2])+2,1);
        x=kth(i,1);
        father[son[root][2]]=0;
        y=cnt[son[root][1]];
        root=son[root][2];
        //l=findnum(a[i][2])+2;
        splay(l);
        father[l]=x;
        son[x][2]=l;
        root=x;
        lazy[son[l][1]]^=1;
    }
    return 0;
}
