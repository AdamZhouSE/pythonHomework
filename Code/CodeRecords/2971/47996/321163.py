#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#define N 1000005
using namespace std;
char s[N];
int n,m,sa[N],rk[N],tp[N],tax[N];

void rsort(){
	for(int i=1;i<=m;i++) tax[i]=0;
	for(int i=1;i<=n;i++) ++tax[rk[i]];//加入桶 
	for(int i=1;i<=m;i++) tax[i]+=tax[i-1];//求前缀 
	for(int i=n;i;i--) sa[tax[rk[tp[i]]]--]=tp[i];//倒序按第二关键字排序 
}

void ssort(){
	for(int i=1;i<=n;i++) rk[i]=s[i],tp[i]=i;
	rsort();//长度为1 
	for(int w=1,p=0;p<n && w<=n;m=p,w<<=1){
		p=0;//w为长度，p为计数器 
		for(int i=n-w+1;i<=n;i++) tp[++p]=i;//n-w+1~n,第二关键字最小 
		for(int i=1;i<=n;i++)
			if(sa[i]>w) tp[++p]=sa[i]-w;//要在一个后缀后面接一个后缀 
		rsort(); 
		swap(rk,tp);//备份 
		rk[sa[1]]=p=1;
		for(int i=2;i<=n;i++){
			if(tp[sa[i]]==tp[sa[i-1]] && tp[min(n+1,sa[i]+w)]==tp[min(n+1,sa[i-1]+w)])
				rk[sa[i]]=p;//如果第一关键字和第二关键字都和上一个一样 
			else rk[sa[i]]=++p;
		}
	}
}

int main(){
	scanf("%s",s+1); n=strlen(s+1); m=127;
	ssort();
	for(int i=1;i<=n;i++) printf("%d ",sa[i]);
	return 0; 
}