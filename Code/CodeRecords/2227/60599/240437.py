#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <string>
#include <climits>
#include <algorithm>
#include <sstream>
#include <functional>
#include <bitset>
#include <numeric>
#include <cmath>
#include <regex>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <array>
using namespace std;



class Solution 
{
public:
    string crackSafe(int n, int k) 
    {
        string res = string(n, '0');
        unordered_set<string> s;
        s.insert(res);
        for (int i = 0; i < pow(k, n); i++)
        {
            string tmp = res.substr(res.length() - n + 1, n - 1);
            for (int j = k -1;j >= 0; j--)
            {
                string key = tmp + to_string(j);
                if (s.find(key) == s.end())
                {
                    res += to_string(j);
                    s.insert(key);
                    break;
                }
            }
        }
        return res;
    }
};
