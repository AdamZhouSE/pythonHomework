### 题目描述

Bessie 计划调查N (2 <= N <= 2,000)个农场的干草情况，它从1号农场出发。农场之间总共有M (1 <= M <= 10,000)条双向道路，所有道路的总长度不超过1,000,000,000。有些农场之间存在着多条道路，所有的农场之间都是连通的。

Bessie希望计算出该图中最小生成树中的最长边的长度。

### 输入描述

```
两个整数N和M。

接下来M行，每行三个用空格隔开的整数A_i， B_i和L_i，表示A_i和 B_i之间有一条道路长度为L_i。
```
### 输出描述

```
一个整数，表示最小生成树中的最长边的长度。
```

### 测试样例
#### 样例1:输入-输出-解释

```
3 3
1 2 23
2 3 1000
1 3 43
```
```
43
```
```
无
```

### 题目来源  
`luogu.com.cn`