### 题目描述

维护一个数列{a[i]}，支持两种操作：

1、1 L R K D：给出一个长度等于R-L+1的等差数列，首项为K，公差为D，并将它对应加到a[L]~a[R]的每一个数上。即：令a[L]=a[L]+K，a[L+1]=a[L+1]+K+D，

a[L+2]=a[L+2]+K+2D……a[R]=a[R]+K+(R-L)D。

2、2 P：询问序列的第P个数的值a[P]。


### 输入描述

```
第一行两个整数数n，m，表示数列长度和操作个数。

第二行n个整数，第i个数表示a[i]（i=1,2,3…,n）。

接下来的m行，表示m个操作，有两种形式：

1 L R K D

2 P 字母意义见描述（L≤R）。
```
### 输出描述

```
对于每个询问，输出答案，每个答案占一行。
```

### 测试样例
#### 样例1:输入-输出-解释

```
5 2
1 2 3 4 5
1 2 4 1 2
2 3
```
```
6
```
```
无
```

### 题目来源  
`luogu.com.cn`