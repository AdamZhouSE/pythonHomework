#include<iostream>
#include<string>
 
using namespace std;
 
int MinEditDistance(string A,string B)
{
    int len_A = A.length();
    int len_B = B.length();
    int D[len_B+1][len_A+1];
    D[0][0]=0;
    for(int i=1;i<=len_A;i++)
    {
        D[0][i]=i;
    }
    for(int i=1;i<=len_B;i++)
    {
        D[i][0]=i;
    }
    for(int i=1;i<=len_B;i++)
    {
        for(int j=1;j<=len_A;j++)
            D[i][j]=min(min(D[i-1][j]+1,D[i][j-1]+1),(A[j-1]==B[i-1]?D[i-1][j-1]:D[i-1][j-1]+1));
    }
    return D[len_B][len_A];
 
}
 
int main()
{
    string A,B;
    cin>>A>>B;
    cout<<MinEditDistance(A,B) <<endl;
 
}
