#pragma GCC optimize(3)//日常开优化。。

#include<bits/stdc++.h>

using namespace std;

inline int read() {//整型快读，暴力必备；
int num=0, f=1; char c=0;
while (!isdigit(c=getchar())) if (c == '-')  f=-1;
while (isdigit(c))
num=(num<<1)+(num<<3)+(c&15), c=getchar();
return num*f;}
int l,t,o;
int a[100010];//a数组表示该色板上的所有点的颜色；
bool u[40];//布尔数组用来判断该颜色是否出现过，方便统计
int main(){
    l=read();t=read();o=read();
    for(register int i=1;i<=l;i++)a[i]=1;//刚开始所以颜色记为1；
        for(register int i=1;i<=o;i++){
        char xx;
        int x,y,z;
        cin>>xx;//输入操作类别；
        x=read();
        y=read();
        if(x>y)swap(x,y);//交换大小，保证x<y，方便之后的上色；
        if(xx=='C'){//若是上色操作
        z=read();
        for(register int j=x;j<=y;j++){
            a[j]=z;//将区间内所有颜色改为所要上的颜色
            }
        }
        if(xx=='P'){//如果为统计操作
            int sum=0;//记得清零！！！以免多次统计出错；
            for(register int j=1;j<=t;j++){
                u[j]=false;//先初始化所有颜色都未出现过；
            }
            for(register int j=x;j<=y;j++){//在制定区间内一个一个枚举
                if(!u[a[j]]){//若该颜色未出现过
                    u[a[j]]=true;//记为已出现过；
                    sum++;//出现颜色种类加1；
                }
            }
        cout<<sum<<endl;//输出所得数，记得换行。
        }
    }
    return 0;//愉快地结束了主程序；
}