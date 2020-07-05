#include<stdio.h>
int main(){
    /*
    n表示本组用例：有n袋甜饼干
    a[i]表示存放第i个袋子里甜饼干的个数
    evenc为“几袋装有偶数个甜饼干”计数
    sum计算本组用例中所有袋子里甜饼干的数量
    */
    int i,n,evenc,sum,a[100];
    while(~scanf("%d",&n)){ // 多组测试用例
        sum=evenc=0; // 重新开始求和与计数
        for(i=0;i<n;i++){ // 第i+1个袋子
            scanf("%d",&a[i]); // 袋中甜饼干个数
            sum+=a[i]; // 累加袋中甜饼干的数量
            if(a[i]%2==0) evenc++; // 如果甜饼干的数量为偶数
        }
        /*
        1.和为偶数，拿走其中一个偶数或者没有偶数可拿，和仍为偶数，
        evenc袋偶数个甜饼干，evenc种拿法，如果只有奇数，evenc为0；
        2.和为奇数，拿走其中一个奇数，和为偶数，
        n-evenc袋奇数个甜饼干，n-evenc种拿法；
        */
        if(sum%2==0) printf("%d\n",evenc);
        else printf("%d\n",n-evenc);
        /*在和为奇数的情况下，还没有发现“无法拿走任何一袋甜饼干”需要显示0的情况*/
    }
    return 0;
}