### 题目描述

给定一颗有根树，根为 11 ，有以下两种操作：

1、标记操作：对某个结点打上标记。（在最开始，只有结点 11 有标记，其他结点均无标记，而且对于某个结点，可以打多次标记。）

2、询问操作：询问某个结点最近的一个打了标记的祖先。（这个结点本身也算自己的祖先）


### 输入描述

```
第一行两个正整数 N 和 Q 分别表示节点个数和操作次数。

接下来 N-1 行，每行两个正整数 u,v(1⩽u,v⩽n) 表示 u 到 v 有一条有向边。

接下来 Q 行，形如 oper num ，oper 为 C 时表示这是一个标记操作, oper 为 Q 时表示这是一个询问操作。
```
### 输出描述

```
输出一个正整数，表示结果
```

### 测试样例
#### 样例1:输入-输出-解释

```
5 5 
1 2 
1 3 
2 4 
2 5 
Q 2 
C 2 
Q 2 
Q 5 
Q 3
```
```
1
2
2
1
```
```
无
```

### 题目来源  
`luogu.com.cn`