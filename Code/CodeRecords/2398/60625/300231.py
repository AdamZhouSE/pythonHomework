#include<iostream>
#include<cstdio>
#include<queue>

using namespace std;

inline int rd(){
  int ret=0,f=1;char c;
  while(c=getchar(),!isdigit(c))f=c=='-'?-1:1;
  while(isdigit(c))ret=ret*10+c-'0',c=getchar();
  return ret*f;
}

const int MAXN=100005;

int n,t;
int d[MAXN];
priority_queue<int> Q;

bool check(int x){
  for(int i=1;i<=x;i++) Q.push(d[i]);
  for(int i=x+1;i<=n;i++){
    int top=Q.top();Q.pop();
    Q.push(top+d[i]);
  }
  int ret=0;
  while(!Q.empty()){ret=max(ret,-Q.top());Q.pop();}
  return ret<=t;
}

int main(){
  n=rd();t=rd();
  for(int i=1;i<=n;i++) d[i]=-rd();
  int l=1,r=n;
  int ans;
  while(l<=r){
    int mid=(l+r)>>1;
    if(check(mid))r=mid-1,ans=mid;
    else l=mid+1;
  }
  printf("%d\n",ans);
  return 0;
}