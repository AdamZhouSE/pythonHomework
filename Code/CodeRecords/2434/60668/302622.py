#include<cstdio>
#define MAXN 1000001
using namespace std;
bool p;
int n,m,c,dui1[MAXN],dui2[MAXN],a[MAXN],heada=1,taila=0,headb=1,tailb=0;
int main(){
    scanf("%d%d%d",&n,&m,&c);
    for(int i=1;i<=n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=1;i<=n;i++){
        while(heada<=taila&&dui1[heada]+m<=i){
            heada++;
        }//这里的两个while的意思是如果最大值的位置不在所要寻找最大值的序列当中，就把它踢出去,反正是从左往右找吗
        while(headb<=tailb&&dui2[headb]+m<=i){
            headb++;
        } 
        while(heada<=taila&&a[i]>a[dui1[taila]]){
            taila--;
        } //这里的两个while能够减小时间复杂度,先把已经比要插入的小或大踢出去     
        dui1[++taila]=i;
        while(headb<=tailb&&a[i]<a[dui2[tailb]]){
            tailb--;
        } 
        dui2[++tailb]=i;
        if(i>=m){
            if(a[dui1[heada]]-a[dui2[headb]]<=c){
                printf("%d\n",i-m+1);
                p=true;
            }
        }
    }
    if(!p) printf("NONE");
    return 0;
}