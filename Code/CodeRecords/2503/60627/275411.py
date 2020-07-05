#ifndef C717_H
#define C717_H
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    /*
    * @param : as indicated in the description
    * @param : as indicated in the description
    * @return: Return the number of edges on the longest path with same value.
    */
    int LongestPathWithSameValue(vector<int> &A, vector<int> &E) {
        // write your code here
        if (A.size() == 1)
            return 0;
        vector<vector<int>> nums(A.size()+1);
        vector<int> v(A.size(), 0);
        for (int i = 0; i < E.size(); i = i + 2)
        {
            nums[E[i]].push_back(E[i + 1]);
            v[E[i + 1]-1] = 1;
        }
        int root = 0;
        for (int i = 0; i < A.size(); ++i)
        {
            if (v[i] == 0)
                root = i + 1;
        }
        int num = 0;
        CountPath(nums, A, root, num);
        return num;
    }
    int CountPath(vector<vector<int>> nums, vector<int> A, int root, int &res)
    {
        if (nums[root].size() == 0)
            return 0;
        vector<int> tmp(nums[root].size(), 0);
        for (int i = 0; i < nums[root].size(); ++i)
        {
            tmp[i] = CountPath(nums, A, nums[root][i], res);
        }
        for (int i = 0; i < nums[root].size(); ++i)
        {
            if (A[root - 1] == A[nums[root][i] - 1])
                tmp[i] = tmp[i] + 1;
            else
                tmp[i] = 0;
        }
        sort(tmp.begin(), tmp.end());
        if (nums[root].size() == 1)
            res = maxVal(res, tmp[0]);
        else
            res = maxVal(res, tmp[nums[root].size() - 1] + tmp[nums[root].size() - 2]);
        return tmp.back();
    }
    int maxVal(int a, int b)
    {
        return a > b ? a : b;
    }
};
#endif