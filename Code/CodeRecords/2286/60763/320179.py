#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){

    int L,M,sum,left,right,i;//sum is the sum of the trees

    while(scanf("%d%d",&L,&M),L!=0){
        int road[10001]={};
        sum=0;
        while(M--){
            scanf("%d%d",&left,&right);

            fill(road+left,road+right+1,1);
        }
        for(i=0;i<=L;i++)
        {
            if(road[i]==0)
                sum++;
        }
        printf("%d\n",sum);
    }
    return 0;
}
