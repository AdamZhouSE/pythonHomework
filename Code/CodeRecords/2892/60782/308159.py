#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int a[17],n,m;
int main (){
    scanf("%d %d",&n,&m);
    for(int i=n;i<=m;i++){
        int jjj=i;
        while(jjj>0){
            a[jjj%10]++;
            jjj/=10;
        }
    }
    for(int i=0;i<=9;i++)
        printf ("%d ",a[i]);
    return 0;
}