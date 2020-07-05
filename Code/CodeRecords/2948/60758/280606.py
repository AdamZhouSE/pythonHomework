#include <cstdio>
#include <cstring>
using namespace std;
 
char s[20];
int num[50];
int st,len,tot;
 
int read() {
    int x=0,f=1;char ch=getchar();
    for(;ch<'0'||ch>'9';ch=getchar())if(ch=='-')f=-1;
    for(;ch>='0'&&ch<='9';ch=getchar())x=(x<<1)+(x<<3)+ch-'0';
    return x*f;
}
 
void add(int n) {
    int a[10],cnt=0;
    memset(a,0,sizeof(a));
    while(n) a[++cnt]=n%10,n/=10;
    for(int i=cnt;i;i--) num[++tot]=a[i];//开了辅助数组a后，妈妈再也不用担心我写4个if语句了
}
 
int main() {
    scanf("%s",s+1);
    st=read();
    len=strlen(s+1);
    for(int i=1;i<=len;i++)
        add(s[i]-'A'+st);//把对应字母转成数字
    while(tot>3) {
        for(int i=1;i<tot;i++)
            num[i]=(num[i]+num[i+1])%10;
        tot--;
    }//模拟每次合并的过程
    if(num[1]==1&&num[2]==0&&num[3]==0)puts("100");
    else printf("%d",(num[1]+num[2])%10*10+(num[2]+num[3])%10);//特判结果
    return 0;
}