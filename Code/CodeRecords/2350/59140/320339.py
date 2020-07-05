#include<bits/stdc++.h>
using namespace std;

const int MAXN=105;
const int INF=1e9+7;

inline int mymin(int x,int y){return x>y?y:x;}

int a[MAXN],b[MAXN],c[MAXN],n,tot=0;
int chuli[MAXN],shuzu[MAXN],shang[MAXN],xia[MAXN],ans,output;
bool vis[MAXN];

void fre(){
    freopen("1.in","r",stdin);
}

void dfs(int o){
    if(ans>output)return;
//  cout<<o<<":"<<endl;
//  for(int i=1;i<=tot;i++)cout<<shang[i];
//  cout<<endl;
//  for(int i=1;i<=tot;i++)cout<<xia[i];
//  cout<<endl<<":::"<<ans;
//  cout<<endl<<endl;
    if(o==tot){
        output=mymin(ans,output);
        return; 
    }
    if(!vis[o]){
        int tmp=shuzu[o],tans=0,t1=0,tans2=0,t2=0,zd,tmp2;
        for(int i=o+1;i<=tot;i++){//从上面走 
            if(shuzu[i]==tmp){
                t1=tans;t2=tans2;zd=i;
            }
            if(shang[i])tans++; 
            if(xia[i])tans2++;//从下面走 
        }
        for(int i=tot;;i--){
            if(shuzu[i]==tmp)break;
            if(xia[i])tans++;
            if(shang[i])tans2++;
        }
        tmp2=mymin(t1,t2);
        tmp2=mymin(tmp2,mymin(tans,tans2));
        if(t1<tans2){
            ans+=t1;shang[zd]++;vis[zd]=1;
            dfs(o+1);
            ans-=t1;shang[zd]--;vis[zd]=0;
        }
        else {
            ans+=tans2;shang[zd]++;vis[zd]=1;
            dfs(o+1);
            ans-=tans2;shang[zd]--;vis[zd]=0;
        }
        if(t2<tans){
            ans+=t2;xia[zd]++;vis[zd]=1;
        //  cout<<tmp<<"->"<<t2<<"***:"<<ans<<":"<<zd<<endl;
            dfs(o+1);
            ans-=t2;xia[zd]--;vis[zd]=0;
        }
        else{
            ans+=tans;xia[zd]++;vis[zd]=1;
            dfs(o+1);
            ans-=tans;xia[zd]--;vis[zd]=0;
        }
    }
    else dfs(o+1);
}
/*
1
8
1 2 3 4 1 3 2 4
*/ 

void mem(){
    memset(a,0,sizeof(a));
    memset(b,0,sizeof(b));
    memset(c,0,sizeof(c));
    memset(chuli,0,sizeof(chuli));
    memset(shuzu,0,sizeof(shuzu));
    memset(vis,0,sizeof(vis));
    memset(shang,0,sizeof(shang));
    memset(xia,0,sizeof(xia));
    tot=0,ans=0;output=INF;
}

int sp=0;
void work(){
    mem();
    scanf("%d",&n);
    int pre;
    for(int i=1;i<=n;i++){
        pre=a[i-1];
        scanf("%d",&a[i]);  
        if(pre!=a[i])chuli[a[i]]++;
    }
    for(int i=1;i<=n;i++)
        if(chuli[a[i]]==2)shuzu[++tot]=a[i];
    if(!tot)printf("0\n");
    else {
        dfs(1);
        printf("%d\n",output);  
    }
}

int main(){
//  fre();
    int T;
    scanf("%d",&T);
    while(T--)work();
    return 0;
}