### 题目描述

面对蚂蚁们的疯狂进攻，小FF的Tower defence宣告失败……人类被蚂蚁们逼到了Greed Island上的一个海湾。现在，小FF的后方是一望无际的大海， 前方是变异了的超级蚂蚁。 小FF还有大好前程，他可不想命丧于此， 于是他派遣手下最后一批改造SCV布置地雷以阻挡蚂蚁们的进攻。

小FF最后一道防线是一条长度为N的战壕， 小FF拥有无数多种地雷，而SCV每次可以在[ L , R ]区间埋放同一种不同于之前已经埋放的地雷。 由于情况已经十万火急，小FF在某些时候可能会询问你在[ L' , R'] 区间内有多少种不同的地雷， 他希望你能尽快的给予答复。

### 输入描述

```
第一行为两个整数n和m； n表示防线长度， m表示SCV布雷次数及小FF询问的次数总和。

接下来有m行， 每行三个整数Q，L , R； 若Q=1 则表示SCV在[ L , R ]这段区间布上一种地雷， 若Q=2则表示小FF询问当前[ L , R ]区间总共有多少种地雷。
```
### 输出描述

```
对于小FF的每次询问，输出一个答案（单独一行），表示当前区间地雷总数。
```

### 测试样例
#### 样例1:输入-输出-解释

```
5 4
1 1 3
2 2 5
1 2 4
2 3 5
```
```
1
2
```
```
无
```

### 题目来源  
`luogu.com.cn`