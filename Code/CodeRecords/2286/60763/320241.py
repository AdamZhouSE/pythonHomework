#include<string.h>
#include<ctype.h>
#include<stdio.h>

int main() {
    int l,m,i,j,k,count;
    int flag[10010],num1,num2;
    while(scanf("%d",&l)!=EOF){
        count=0;
        for(i=0;i<10010;i++)
            flag[i]=0;
        for(i=0;i<=l;i++)
            flag[i]=1;

        scanf("%d",&m);
        for(i=0;i<m;i++) {
            scanf("%d%d", &num1, &num2);
            for (j = num1; j <= num2; j++) {
                flag[j] = 0;
            }
        }
        for(i=0;i<=l;i++)
            if(flag[i]==1){
                count++;
            }              
        printf("%d\n",count);
    }                    
    return 0;
}