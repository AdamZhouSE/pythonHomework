#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;
int gcd(int a,int b){
	return b==0?a:gcd(b,a%b);
}
int Cross(int x1,int y1,int x2,int y2){
	return x1*y2-x2*y1;
}
int main(){
	int t;
    scanf("%d",&t);
    int x1,y1,x2,y2,x3,y3;
	while(t-- > 0){
		scanf("%d%d%d%d%d%d",&x1,&y1,&x2,&y2,&x3,&y3);
        if(!x1&&!y1&&!x2&&!y2&&!x3&&!y3) break;
		int cnt=gcd(abs(x1-x2),abs(y1-y2));
		cnt+=gcd(abs(x1-x3),abs(y1-y3));
		cnt+=gcd(abs(x2-x3),abs(y2-y3));
		int S=abs(Cross(x1-x2,y1-y2,x1-x3,y1-y3))/2;
		printf("%d\n",S-cnt/2+1);
	}
	return 0;
}