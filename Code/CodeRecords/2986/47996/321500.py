#include <string.h>
#include <iostream>
using namespace std;
/*将字符串A转换为字符串B最少的操作次数*/ 
int minEditDistance(string A,string B)
{
    int A_len=A.length();
    int B_len=B.length();
    int D[B_len+1][A_len+1];
    D[0][0]=0;
    for(int i=1;i<=A_len;i++)
    {
        D[0][i]=i;
    } 
    for(int i=1;i<=B_len;i++)
    {
        D[i][0]=i;
    }  
    for(int i=1;i<=B_len;i++)
    {
        for(int j=1;j<=A_len;j++)
            D[i][j]=min(min(D[i-1][j]+1,D[i][j-1]+1),(A[j-1]==B[i-1]?D[i-1][j-1]:D[i-1][j-1]+1));
    } 
    return D[B_len][A_len];
}

int main()
{
    string A,B;
    cin>>A>>B;
    cout<<minEditDistance(A,B)<<endl;
}