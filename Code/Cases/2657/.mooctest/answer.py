#include <cstdio>
const int MAXN=100010;
struct P {
    bool ty;
    int id,ans;
}p[MAXN];
int edv[MAXN<<1],ednxt[MAXN<<1];
int first[MAXN],cnt=0;
void add(int x,int y) {
    edv[++cnt]=y;
    ednxt[cnt]=first[x];
    first[x]=cnt;
}
int col[MAXN];
char inp[3];
int ufs[MAXN];  //并查集数组
int f[MAXN];    //记录一个点的父亲
void dfs(int x,int fa) {
    if(col[x]) ufs[x]=x;   //如果有染色，就让值等于自己
    else ufs[x]=fa;        //否则等于父亲
    f[x]=fa;
    for(int i=first[x];i;i=ednxt[i]) {
        int v=edv[i];
        if(v==fa) continue;
        dfs(v,x);
    }
}
int find(int x) {
    return x==ufs[x]?x:ufs[x]=find(ufs[x]);
}
int main() {
    int n,q;
    scanf("%d%d",&n,&q);
    int in1,in2;
    for(int i=1;i<n;++i) {
        scanf("%d%d",&in1,&in2);
        add(in1,in2);
        add(in2,in1);
    }
    col[1]=1;
    for(int i=1;i<=q;++i) {
        scanf("%s%d",inp,&p[i].id);
        switch(inp[0]) {
            case 'Q':{
                p[i].ty=0;
                break;
            }
            case 'C':{
                p[i].ty=1;
                ++col[p[i].id];
                break;
            }
        }
    }
    dfs(1,0);
    f[1]=1;
    for(int i=q;i>=1;--i) {
        if(p[i].ty) {
            --col[p[i].id];
            if(!col[p[i].id]) ufs[p[i].id]=f[p[i].id];  //这个点没有染色了
        } else {
            p[i].ans=find(p[i].id);
        }
    }
    for(int i=1;i<=q;++i) {
        if(!p[i].ty) {
            printf("%d\n",p[i].ans);
        }
    }
    return 0;
}