#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
int main()
{
    int n,k;
    int *p;
    int i=0,j,count=0;
    scanf("%d %d",&n,&k);
    p=(int*)malloc(sizeof(int)*n);//用的动态数组 
    j=n-1;
    for(i=0;i<n;i++)
    {
        scanf("%d",&p[i]);//保存孩子们的体重
    }
/*除去全部被甩下去的情况*/
    for(i=0;i<n;i++)//从左到右的遍历
        {
            if(p[i]<=k)
                count++;//计数
            else
                break;
        }
    for(i=n-1;i>=0;i--)
    {
        if(p[i]<=k)
            count++;
        else
            break;
    }
/*全部被甩下去的情况*/
    if(count/n==2)
        count=n;
    printf("%d\n",count);
    free(p);
    return 0;
 
}