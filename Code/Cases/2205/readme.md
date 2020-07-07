## 题目描述
We have N persons sitting on a round table. Any person can do a handshake with any other person.

        1
    
    2        3

        4
我们有N个人坐在圆桌旁。任何人都可以与任何其他人握手。2-3和1-4握手会导致交叉。 这N个人可以通过多种方式进行握手，这样就不会有两次握手发生交叉。 N会是偶数。 例如，在上图中，有两种非交叉方式来握手{{1，2}，{3，4}}和{{1，3}，{2，4}}。
## 输入描述
输入的第一行包含一个整数T，它表示测试用例的数量。 每个测试用例的第一行是N。1 ≤ T ≤ 20;
2 ≤ N ≤ 30
## 输出描述
打印方式的数目。
## 样例输入
2

2

8
## 样例输出
1

14
## 题目来源
geeksforgeeks.org