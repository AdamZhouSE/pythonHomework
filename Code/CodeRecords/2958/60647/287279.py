#include<bits/stdc++.h>
using namespace std;
const int max_n=100+5;
int n,g[max_n],f[max_n][max_n]; 
string st;
bool check(int ll,int rr,int len){//判断是否是循环节 
    for(int i=ll;i<=ll+len-1;i++){
        char ch=st[i];
        for(int j=i;j<=rr;j+=len){
            if(st[j]!=ch)return false;
        }
    }
    return true;
}
int main(){
    ios::sync_with_stdio(false);
    cin>>st;
    n=st.size();st=" "+st;//把字符串变成1~n 
    for(int i=1;i<=9;i++)g[i]=1;
    for(int i=10;i<=99;i++)g[i]=2;
    g[100]=3;//g[x]表示x的位数 
    memset(f,0x3f,sizeof(f));
    for(int i=1;i<=n;i++)f[i][i]=1;//初始化f数组 
    for(int len=1;len<=n;len++){
        for(int i=1;i+len-1<=n;i++){
            int j=i+len-1;//区间DP模板，得到i和j 
            for(int k=i;k<j;k++){//枚举哪里切 
                f[i][j]=min(f[i][j],f[i][k]+f[k+1][j]);//第一种情况，左区间+右区间 
                int l=k-i+1;//第二种情况，先得到循环节的长度 
                if(len%l)continue;//长度不符 
                if(check(i,j,l))f[i][j]=min(f[i][j],g[len/l]+2+f[i][k]);//是循环节，那么套公式 
            }
        }
    }
    cout<<f[1][n]<<"\n"; 
    return 0;
}