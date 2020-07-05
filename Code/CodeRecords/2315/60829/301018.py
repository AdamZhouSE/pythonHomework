
#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int n;
    while(cin >> n)
    {
        int h=1,f,c,temp;
        vector<int> nodeH(1000,0);
        vector<int> cNum(1000,0);
        bool isFather = true;
        while(n--)
        {
            cin >> f >> c;
            if(isFather)
            {
                nodeH[f] = 1;
                isFather = false;
            }
            if(nodeH[f] == 0 || cNum[f] == 2)
                continue;
            cNum[f] += 1;
            temp = nodeH[f] + 1;
            nodeH[c] = temp;
            if(temp > h) h = temp;
        }
        cout << h<<endl;
    }
    return 0;
}