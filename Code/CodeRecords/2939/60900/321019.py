#include<iostream>
#include<string>
#include<cstdio>
#include<algorithm>
#include<sstream>
using namespace std;
typedef long long ll;
ll num[30010]={0,1};
int main(){
    int n, m, front, cnt, end;
    ll a, b;
    scanf("%d%d",&n,&m);
    int i = 1, j = 1;
    for (int k = 2; k <= n; k++){
        a = num[i] * 2 + 1;
        b = num[j] * 4 + 5;
        if (a > b) j++,num[k] = b;
        else if (a == b) i++,j++,num[k] = a;
        else i++,num[k] = a;
    }
    string s = "", ans = "";
    for(i = 1; i <= n; i++){
        stringstream ss;string str;
        ss << num[i];ss >> str;
        s += str;
    }
    cout<<s<<endl;
    string::iterator it = s.begin();s.insert(it, '9');
    n = s.size();front = cnt = 0;end = 1;
    while (end <= n && cnt != m){
        if (s[end] <= s[front]) s[++front] = s[end++];
        else front--,cnt++;
    }
    while (end <= n) s[++front] = s[end++];
    for (i = 1; i < n - m; i++) printf("%c",s[i]);
    fclose(stdin);fclose(stdout);
	return 0;
}