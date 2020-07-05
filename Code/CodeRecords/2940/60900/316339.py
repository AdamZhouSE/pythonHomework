#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int N=110;
int f[N][N];
string c[N][N],s;

bool Judge(int l,int r,int length) {
    if ((r-l+1)%length) return 0;
    for (int i=1;i<=r-l+1;i++)
        if (s[l+i-1]!=s[l+(i-1)%length]) return 0;
    return 1;
}

int Digit(int num) {
    int ans=0;
    while (num) {
        ans++;
        num/=10;
    }
    return ans;
}

string Change(int num) {
    string s="";
    while (num) {
        s+=(num%10+48);
        num/=10;
    }
    for (int i=0;i<s.length()/2;i++) {
        char c=s[i];
        s[i]=s[s.length()-i-1];
        s[s.length()-i-1]=c;
    }
    return s;
}

void Solve(int l,int r) {
    if (f[l][r]) return;
    if (l==r) {
        f[l][r]=1;
        c[l][r]+=s[l];
        return;
    }
    f[l][r]=r-l+1;
    for (int i=l;i<=r;i++) c[l][r]+=s[i];
    for (int i=l;i<r;i++) {
        Solve(l,i);Solve(i+1,r);
        if (f[l][r]>f[l][i]+f[i+1][r]) {
            f[l][r]=f[l][i]+f[i+1][r];
            c[l][r]=c[l][i]+c[i+1][r];
        }
    }
    for (int i=1;i<=r-l;i++)
        if (Judge(l,r,i)) {
            Solve(l,l+i-1);
            if (f[l][r]>f[l][l+i-1]+2+Digit((r-l+1)/i)) {
                f[l][r]=f[l][l+i-1]+2+Digit((r-l+1)/i);
                c[l][r]=Change((r-l+1)/i)+"("+c[l][l+i-1]+")";
            }
        }
}

int main() {
    cin>>s;
    Solve(0,s.length()-1);
    cout<<c[0][s.length()-1]<<endl;
}