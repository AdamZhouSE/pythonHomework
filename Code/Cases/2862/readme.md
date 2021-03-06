### 题目描述

Polycarp 有一个长度为 n 的整数数组。

他想在数组上玩个游戏。 游戏由几步组成:

- 第一步，他选择任一元素并将其删除（第一步之后，数组包含n−1个元素）。 
- 对于接下来的每个操作，他都在限定规则下选择任一元素：
  - 若上一个删除的是奇数，则这次只能删除偶数
  - 若上一个删除的是偶数，则这次只能删除奇数
- 但无法在进行下一步时，游戏结束

Polycarp 的目标是在游戏结束后最大程度地减少数组中未删除元素的总和。 如果 Polycarp 可以删除整个数组，则未删除元素的总和为零。 帮助 Polycarp 找到最小值。

### 输入描述

```
第一行输入一个整数 n (1 <= n <= 2000)代表数组a的长度
第二行输入 n 个数，分别代表 a[1], a[2], a[3]…. a[n] (0 <= a[i] <= 1000000)
```

### 输出描述

```
输出一个数代表最小的未删除元素的总和
```

### 测试样例

#### 样例1: 输入-输出

```
5
1 5 7 8 2
```

```
0
```

#### 样例2: 输入-输出

```
6
5 1 2 4 6 3
```

```
0
```

#### 样例3: 输入-输出

```
2
1000000 1000000
```

```
1000000
```

### 题目来源

CodeForces
