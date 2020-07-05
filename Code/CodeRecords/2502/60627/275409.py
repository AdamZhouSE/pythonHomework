#include<stdio.h>
#include<iostream>
using namespace std;
const int N=1000005;
int t[N]={0x7fffffff},top;
int main(){
	int n,x;
	long long ans=0;
	scanf("%d",&n);
	while(n--){
		scanf("%d",&x);
		while(top&&x>=t[top]){
			if(t[top-1]<x){
				ans+=t[top-1];
			}
			else{
				ans+=x;
			}
			--top;
		}
		t[++top]=x;
	}
	while(top>1){
		ans+=t[--top];
	}
	printf("%lld\n",ans);
	return 0;
}