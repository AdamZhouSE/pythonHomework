#include <iostream>
#include <list>
#include <algorithm>
#include <tuple>
#include <cmath>
#include <iomanip>
#include <vector>
#include <numeric>

#ifdef DEBUG
#include <sstream>
std::stringstream stin(R"__(2 4
0 100
0 300
0 600
150 750
)__");
#else
#define stin std::cin
#endif // DEBUG

using edge = std::tuple<double, int, int>;
constexpr int maxn = 505;
int S, P;
std::vector<edge> gra, tree;
int p[maxn];
std::pair<double, double> pos[maxn];

constexpr double EuclidDistance(std::pair<int, int> p1, std::pair<int, int> p2)
{
    return std::sqrt((p1.first - p2.first)*(p1.first - p2.first)+(p1.second - p2.second)*(p1.second - p2.second));
}

int find(int pos)
{
    return p[pos] == pos ? pos : p[pos] = find(p[pos]);
}

int main()
{
    stin >> S >> P;
    for(int i = 1; i <= P; i++)
        stin >> pos[i].first >> pos[i].second;
    std::iota(p+1, p+1+P, 1);
    for(int i = 1; i <= P - 1; i++)
        for(int j = i+1; j <= P; j++)
        {
            auto dis = EuclidDistance(pos[i], pos[j]);
            gra.emplace_back(dis, i, j);
            gra.emplace_back(dis, j, i);
        }
    std::sort(gra.begin(), gra.end());
    int count = 0;
    for(auto& i : gra)
    {
        if(find(std::get<1>(i))!=find(std::get<2>(i)))
        {
            p[p[std::get<1>(i)]] = p[std::get<2>(i)];
            count++;
        }
        if(count == P - S)
        {
            std::cout << std::fixed << std::setprecision(2) << std::get<0>(i) << std::ends;
            return 0;
        }
    }
}