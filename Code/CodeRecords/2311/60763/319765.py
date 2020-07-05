#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
using namespace std;

void sumtree(vector<int> &inorder, int left, int right){
    int mid = (left + right)/2;
    if(mid == left) {
        inorder[mid] = 0;
        return;
    }
    inorder[mid] = accumulate(inorder.begin()+left, inorder.begin()+right, -inorder[mid]);
    sumtree(inorder, left, mid);
    sumtree(inorder, mid+1, right);
}

int main(void) {
    string line;
    getline(cin, line);
    istringstream pre_stream(line);
    vector<int> preorder((istream_iterator<int>(pre_stream)), istream_iterator<int>());
    getline(cin, line);
    istringstream in_stream(line);
    vector<int> inorder((istream_iterator<int>(in_stream)), istream_iterator<int>());
    sumtree(inorder, 0, inorder.size());
    copy(inorder.begin(), inorder.end(),ostream_iterator<int>(cout, " "));
    cout<<"";
    return 0;
}