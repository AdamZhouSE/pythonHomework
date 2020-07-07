#include<iostream>
    #include<cstdlib>
    #include<cstdio>
    #include<cmath>
    #include<cstring>
    #include<iomanip>
    #include<algorithm>
    #include<stack>
    #include<queue>
    #define lst long long
    #define rg register
    #define N 100050
    using namespace std;
    int n,m;
    lst ans;
    int tou[N],wei[N];//tou存前面有多少个区间的开始，以下简称头部树状数组
                      //wei存前面有多少个区间的尾部，以下简称尾部树状数组
                      //类似于前缀和
    inline int read()//读入优化
    {
        rg int s=0,m=1;rg char ch=getchar();
        while(ch!='-'&&(ch<'0'||ch>'9'))ch=getchar();
        if(ch=='-')m=-1,ch=getchar();
        while(ch>='0'&&ch<='9')s=(s<<3)+(s<<1)+ch-'0',ch=getchar();
        return s*m;
    }
    //以下是树状数组的板子
    inline int lowbit(rg int kk)//lowbit
    {
        return kk&(-kk);
    }
    inline void add_tou(rg int kk)//加入树状数组的头部数组
    {
        while(kk<=n)
        {
            ++tou[kk];
            kk+=lowbit(kk);
        }
    }
    inline void add_wei(rg int kk)//加入树状数组的尾部数组
    {
        while(kk<=n)
        {
            ++wei[kk];
            kk+=lowbit(kk);
        }
    }
    inline int sum_tou(rg int kk)//计算节点前有多少个区间的开始
    {
        rg int s=0;
        while(kk>0)
        {
            s+=tou[kk];
            kk-=lowbit(kk);
        }
        return s;
    }
    inline int sum_wei(rg int kk)//计算节点前有多少个区间的结束
    {
        rg int s=0;
        while(kk>0)
        {
            s+=wei[kk];
            kk-=lowbit(kk);
        }
        return s;
    }
    int main()
    {
        n=read(),m=read();//读入
        for(rg int i=1;i<=m;++i)
        {
            rg int sign=read();
            rg int x=read(),y=read();//读入
            if(sign==1)
            {
                add_tou(x);//加入头部树状数组
                add_wei(y);//加入尾部树状数组
            }
            else
            {
                ans=sum_tou(y)-sum_wei(x-1);//运用已经证明的规律结题
                printf("%d\n",ans);
            }
        }
        return 0;
    }