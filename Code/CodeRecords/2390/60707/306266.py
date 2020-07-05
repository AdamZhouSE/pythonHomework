
#include<cstdio>

#include<iostream>

#include<cstdlib>

#include<cstring>

#include<algorithm>

#include<cmath>

using namespace std;

int n,N,s[1<<13],fac[22],ans;

bool pd(int l,int r){

    bool fl=1;

    for(int i=l;i<r;i++){

        if(s[i]+1!=s[i+1]){fl=0;break;}

    }

    return fl;

}

void work(int x,int y,int l){

    for(int i=x,j=y;l;l--,i++,j++)swap(s[i],s[j]);

}

void dfs(int k,int op,int ff){

    if(k==n){

        ans+=fac[op];return;

    }

    int now=(1<<k+1),sum=0,nn=(1<<k),b[5];

    for(int j=1;j<=N;j+=now){

        if(!pd(j,j+now-1)){

            b[++sum]=j; 

            if(sum==3)return; 

        }

    }

    if(sum==0){dfs(k+1,op,-1);return;}

    if(sum>3)return;

    if(sum==1){

        work(b[1],b[1]+nn,nn);

        if(pd(b[1],b[1]+now-1))dfs(k+1,op+1,0);

        work(b[1],b[1]+nn,nn);

        return;

    }

    if(sum==2){

    work(b[1],b[2],nn);

    if(pd(b[1],b[1]+now-1)&&pd(b[2],b[2]+now-1))dfs(k+1,op+1,1);

    work(b[1],b[2],nn);

     

    work(b[1],b[2]+nn,nn);

    if(pd(b[1],b[1]+now-1)&&pd(b[2],b[2]+now-1))dfs(k+1,op+1,2);

    work(b[1],b[2]+nn,nn);

     

    work(b[1]+nn,b[2],nn);

    if(pd(b[1],b[1]+now-1)&&pd(b[2],b[2]+now-1))dfs(k+1,op+1,3);

    work(b[1]+nn,b[2],nn);

     

    work(b[1]+nn,b[2]+nn,nn);

    if(pd(b[1],b[1]+now-1)&&pd(b[2],b[2]+now-1))dfs(k+1,op+1,4);

    work(b[1]+nn,b[2]+nn,nn);

     

    }

}

int main()

{

    cin>>n;N=(1<<n);

    for(int i=1;i<=N;i++)scanf("%d",&s[i]);

    fac[0]=1;for(int i=1;i<=n;i++)fac[i]=fac[i-1]*i;

    dfs(0,0,-2);

    cout<<ans<<endl;

    return 0;

}
