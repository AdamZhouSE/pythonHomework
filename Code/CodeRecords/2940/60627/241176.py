#include<iostream>
#include<algorithm>
#include<string>
#include<limits.h>
#include<unordered_map>
using namespace std;
 
unordered_map<string, int> mem;
int divid(string str)
{
    if(str.size() < 4) return str.size();
    if(mem.count(str)) return mem[str];
    int len = str.size(), Min = INT_MAX;
    for(int i = 1, j; i <= len/2; i++)
    {
        string tem = str.substr(0, i);
        for(j = 0; j <= len-i; j+= i)
            if(str.substr(j, i) != tem) break;
        if(j >= len)
            return to_string(len/i).size() + 2 + divid(tem);
        if(len == 4) return 4;
    }
    for(int i = 1; i < len; i++)
    {
        string left = str.substr(0, i), right = str.substr(i); 
        int val1 = divid(str.substr(0, i)), val2 = divid(str.substr(i));
        if(left.size() > 3) mem[left] = val1;
        if(right.size() > 3) mem[right] = val2;
        Min = min(Min , val1+val2);
    }
    return Min;
}
 
int main()
{
    string str;
    int T;
    cin >> T;
    while(T--)
    {
        cin >> str;
        cout << divid(str) << endl;
    } 
    return 0;
}