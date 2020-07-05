#include<stdio.h>
#include<math.h>

int main()
{
    int n,rs=1;
    scanf("%d",&n);
    if(n==2){
        printf("1\n");
        return 0;
    }
    if(n==3){
        printf("2\n");
        return 0;
    }
    while(n>4){
        rs*=3;
        n=n-3;
    }
    printf("%d\n",rs*n);
}