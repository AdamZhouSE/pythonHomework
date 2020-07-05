#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,a,b;
int s[100010];
char ch[1010];
bool v;
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
       scanf("%s",ch);
       for(int j=0;j<strlen(ch);j++){
           a=ch[j];
             if(a>='0'&&a<='9') s[i]+=a-'0',s[i]*=10;
             if(a>'9'){
                 if(a=='A'||a=='B'||a=='C') a=2;
                 if(a=='D'||a=='E'||a=='F') a=3;
                 if(a=='G'||a=='H'||a=='I') a=4;
                 if(a=='J'||a=='K'||a=='L') a=5;
                 if(a=='M'||a=='N'||a=='O') a=6;
                 if(a=='P'||a=='R'||a=='S') a=7;
                 if(a=='T'||a=='U'||a=='V') a=8;
                 if(a=='W'||a=='X'||a=='Y') a=9;
                 if(a>1&&a<10) s[i]+=a,s[i]*=10;
             }
         }
        s[i]/=10;
     }
     sort(s+1,s+n+1);
     for(int i=1;i<=n;){
         a=0,b=i;
         while(s[i]==s[b]) a++,i++;
         if(a>1){
             v=1;
             printf("%d%d%d-%d%d%d%d %d\n",s[b]/1000000%10,s[b]/100000%10,s[b]/10000%10,s[b]/1000%10,s[b]/100%10,s[b]/10%10,s[b]%10,a);
         }
     }
     if(!v) printf("No duplicates.");
     return 0;
 }