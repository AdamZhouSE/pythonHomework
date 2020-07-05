#include<cmath>
#include<cstdio>
#include<cstdlib> 
#include<cstring>
#include<iostream>
using namespace std;
char ch[110];
int num,sum,n;
bool p[110];
int main(){
    int i,j;
    scanf("%d\n",&n);
    gets(ch); i=0;
    memset(p,1,sizeof(p));
    while(i<n)
     {
         if(ch[i]=='V'&&ch[i+1]=='K') num++,p[i]=0,p[i+1]=0,i++;
         if(p[i]&&p[i+1]&&ch[i]=='V'&&ch[i+1]!='K'&&i+1<n)
          {
              int t; t=num+1;
              for(j=i+2;j<n-1;++j)
              if(ch[j]=='V'&&ch[j+1]=='K') t++;
            sum=max(sum,t);
          }
        if(p[i]&&p[i-1]&&ch[i]=='K'&&i>0&&ch[i-1]!='V')
         {
             int t; t=num+1;
             for(j=i+1;j<n;++j)
              if(ch[j]=='V'&&ch[j+1]=='K') t++;
             sum=max(sum,t);
         }
        i++;
     }
    sum=max(sum,num);
    printf("%d",sum);
    return 0;
}