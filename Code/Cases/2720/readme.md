### 题目描述

用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

### 输入描述

```
一个整数表示n 台计算机。计算机网络的初始布线 connections。
1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
没有重复的连接。
两台计算机不会通过多条线缆连接。
```
### 输出描述

```
返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。
```

### 测试样例
#### 样例1: 输入-输出-解释
```
4
[[0,1],[0,2],[1,2]]
```
```
1
```
```
拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
```
<p align="">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E8%BF%9E%E9%80%9A%E7%BD%91%E7%BB%9C%E7%9A%84%E6%93%8D%E4%BD%9C%E6%AC%A1%E6%95%B0.png" alt="Sample"  width="500" height="140">
</p>

#### 样例2: 输入-输出-解释
```
6
[[0,1],[0,2],[0,3],[1,2],[1,3]]
```
```
2
```
<p align="">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E8%BF%9E%E9%80%9A%E7%BD%91%E7%BB%9C%E7%9A%84%E6%93%8D%E4%BD%9C%E6%AC%A1%E6%95%B02.png" alt="Sample"  width="600" height="140">
</p>
### 题目来源  
`LeetCode`