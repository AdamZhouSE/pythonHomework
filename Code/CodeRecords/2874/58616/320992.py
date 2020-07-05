
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include<algorithm>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <string>
#include <queue>
#include <stack>
using namespace std;
int a[100];
int main()
{
    int n=0;int num=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(int i=0;i<n-1;i++)
    {
        if(a[i]==0)
            num++;
        else if(a[i]==1)
        {
            if(a[i+1]==1)
                a[i+1]=0;
            else if(a[i+1]==3)
                a[i+1]=2;
        }
        else if(a[i]==2)
        {
            if(a[i+1]==2)
                a[i+1]=0;
            else if(a[i+1]==3)
                a[i+1]=1;
        }
    }
    if(a[n-1]==0)
        num++;
    printf("%d\n",num);
}