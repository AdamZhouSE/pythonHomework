#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
inline int get(){
    int n;char c;while((c=getchar())||1)if(c>='0'&&c<='9')break;
    n=c-'0';while((c=getchar())||1){
        if(c>='0'&&c<='9')n=n*10+c-'0';
        else return(n);
    }
}
typedef struct _n{
    int left;int right;int minn;int adds;int pos;
}node;node memchi[1000001];int gn=1;
int ints[100001];
inline void down(int tree){
    int ls=memchi[tree].left,rs=memchi[tree].right,cjr=memchi[tree].adds;
    if(cjr!=0){memchi[tree].adds=0;
        memchi[ls].minn+=cjr;memchi[rs].minn+=cjr;memchi[ls].adds+=cjr;memchi[rs].adds+=cjr;
    }
}
inline void up(int tree){
    int ls=memchi[tree].left,rs=memchi[tree].right;
    if(memchi[ls].minn<memchi[rs].minn){
        memchi[tree].minn=memchi[ls].minn;
        memchi[tree].pos=memchi[ls].pos;
    }else{
        memchi[tree].minn=memchi[rs].minn;
        memchi[tree].pos=memchi[rs].pos;
    }
}
int build(int l,int r){
    int tree=gn;gn++;memchi[tree].adds=0;
    if(l==r){
        memchi[tree].minn=ints[l];memchi[tree].pos=l;
    }else{
        int mid=(l+r)>>1;memchi[tree].left=build(l,mid);
        memchi[tree].right=build(mid+1,r);up(tree);
    }return(tree);
}
int pt,num;
void setpt(int l,int r,int tree){
    if(l==r){
        memchi[tree].minn=num;return;
    }
    down(tree);int mid=(l+r)>>1;
    if(pt<=mid)setpt(l,mid,memchi[tree].left);
    else setpt(mid+1,r,memchi[tree].right);
    up(tree);
}int n,t;
inline bool check(int mid){gn=1;
    int ptr=mid+1,root=build(1,mid);long long tot=0;
    for(register int i=1;i<=n;i++){
        if(ptr>n){
            tot+=memchi[root].minn;pt=memchi[root].pos;
            int me=memchi[root].minn;memchi[root].minn-=me;memchi[root].adds-=me;
            num=0x7fffffff;setpt(1,mid,root);
        }else{
            tot+=memchi[root].minn;pt=memchi[root].pos;
            int me=memchi[root].minn;memchi[root].minn-=me;memchi[root].adds-=me;
            num=ints[ptr];setpt(1,mid,root);
            ptr++;
        }
    }
    return(tot<=t);
}
int cmp(const int &a,const int &b){
    return(a>b);
}
int main(){
    n=get(),t=get();for(register int i=1;i<=n;i++)ints[i]=get();
    //sort(ints+1,ints+1+n,cmp);
    int ans=0,l=1,r=n;
    while(l<=r){
        int mid=(l+r)>>1;
        if(check(mid)){
            ans=mid;r=mid-1;
        }else l=mid+1;
    }
    cout<<ans<<endl;
    return(0);
}