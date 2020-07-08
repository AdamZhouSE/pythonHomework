### 题目描述

Helen在大都会机场工作，她的任务是安排每天的航班起飞时刻。今天一共有n架飞机将要起飞，第i架飞机将在第i分钟起飞。

大都会机场是大都会最重要的交通枢纽，因此想要原封不动地按照起飞时刻表的时刻起飞是很困难的。今天的情况也是如此：由于技术原因，在今天一开始的k分钟内飞机不允许起飞，因此必须创建一个新的起飞时刻表。

所有的航班必须在第(k+1)分钟到第(k+n)分钟内(包括两端)起飞，而且每分钟仅能有一架飞机起飞。然而，航班起飞的先后顺序可以与最初的时刻表排好的顺序不同，重排的时刻表只有一个限制：飞机不能比它在初始时刻表中起飞的时刻还要早的时刻起飞(即：第i架飞机必须在第i分钟后或第i分钟时起飞)。

Helen知道第i架飞机起飞时刻每延误一分钟机场所需支付的额外花费ci是多少。帮助她找到额外花费最小的方案。

### 输入描述

```
输入数据的第一行包括两个整数n和k(1<=k<=n<=300000)。

第二行包括n个整数c1，c2，...，cn(1<=ci<=10^7)。
```
### 输出描述

```
输出数据的第一行包括一个整数，表示最小额外花费。

第二行包括n个整数t1，t2，...，tn(k+1<=ti<=k+n)，ti表示第i架家航班起飞的时刻。如果同时存在多种方案，输出任意一种。
```

### 测试样例
#### 样例1:输入-输出-解释

```
5 2
4 2 1 10 2
```
```
20
3 6 7 4 5 
```
```
如果Helen仅把每架飞机的起飞时刻都推迟2分钟，那么总额外花费是38。 但是，对于最佳结果来说，总额外花费为20。
(3-1)x4+(4-2)x2+(5-3)x1+(6-4)x10+(7-5)x2=38
(3-1)x4+(6-2)x2+(7-3)x1+(4-4)x10+(5-5)x2=20
```

### 题目来源  
`luogu.com.cn`