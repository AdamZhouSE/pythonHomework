#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
int main(){
    unsigned long i,j,k,n,sum=0;
    int w,**arcs;
    scanf("%ld",&n);
    arcs=(int **)malloc(sizeof(int *)*n);
    arcs[0]=(int *)malloc(sizeof(int)*n*n);
    for(i=1;i<n;++i)arcs[i]=arcs[i-1]+n;//构造n*n的二维数组（邻接矩阵）
    for(i=0;i<n;++i){
        for(j=0;j<n;++j){
            arcs[i][j]=0;
        }
    }//初始化为0
    for(k=1;k<n;++k){
        scanf("%ld%ld%d",&i,&j,&w);
        --i; --j;
        arcs[i][j]=arcs[j][i]=w;
    }//输入最小生成树
    for(i=0;i<n;++i){
        for(j=i+1;j<n;++j){
            if(arcs[i][j]){
                sum+=arcs[i][j];
                continue;
            }
            w=0;
            for(k=0;k<n;++k)if(arcs[i][k]>w)w=arcs[i][k];//查找i行的最大值
            for(k=0;k<n;++k)if(arcs[k][j]>w)w=arcs[k][j];//查找j列比w大的最大值
            sum+=arcs[i][j]=w;
        }
    }
    printf("%lu",sum);
    free(arcs[0]); free(arcs);
    printf("\nFinished!\n");
    getch();
    return 0;
}