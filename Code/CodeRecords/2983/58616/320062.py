#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	int n;
	char s[8005];
	scanf("%d %s",&n,s);
	int k=n-1,flag,ans;
	ans=flag=0;       //ans记录移动的最少的次数 
	for(int i=0;i<k;i++)    //从第一个循环到倒数第二个 
	{
		for(int j=k;j>=i;j--)   //从第K个 向前循环 
		{
			if(j==i)           //i，j相等的时候   表明没有是奇数 
			{
				if(n%2==0||flag==1)     //n为偶数是不允许有一个奇数的字母， 
				{                       //n为奇数时只能有一个奇数的字母 
					printf("Impossible\n");
					return 0;
				}
				flag=1;
				ans=ans+n/2-i;
			}
			else if(s[i]==s[j])      //找到的话 ，求出移动的位置 
			{
				for(int o=j;o<k;o++)
				{
					swap(s[o],s[o+1]);
					ans++;
				}
				k--;
				break;
			}
		}
	}
	printf("%d\n",ans);
	return 0;
 }