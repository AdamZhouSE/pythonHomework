### 题目描述

德武是一个愚蠢的人，他学习很慢。 您需要教他 n 门科目，第 i 门科目有 ci 章。 当您教他时，您应该连续教该科目的所有章节。

起初，他可以在 x 个小时内学习一个章节，如果您教他一门科目，那么教授下一门科目的任何章节所需要的时间将比以前少 1 个小时。 请注意，他每章的学习能力不会少于 1 小时。

您可以按照任何可能的顺序教他 n 个科目。 找出德武最短的学习时间（以小时为单位）。

### 输入描述

```
第一行为科目数量 n 和德武的初始用时 x (1 ≤ n, x ≤ 10^5)
第二行为每门科目的章节数 (1 ≤ ci ≤ 10^5)
```

### 输出描述

```
输出一个整数表示最短的学习时间
```

### 测试样例

#### 样例1: 输入-输出

```
2 3
4 1
```

```
11
```

#### 样例2: 输入-输出

```
4 2
5 1 2 1
```

```
10
```

### 题目来源

CodeForces