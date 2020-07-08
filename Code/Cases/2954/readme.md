### 题目描述

考古学发现，几千年前古梅文明时期的数学非常的发达，他们懂得多位数的加法和乘法，其表达式和运算规则等都与现在通常所用的方式完全相同（如整数是十进制，左边是高位，最高位不能为零；表达式为中缀运算，先乘后加等），唯一的区别是其符号的写法与现在不同。有充分的证据表明，古梅文明的数学文字一共有13个符号，与 0,1,2,3,4,5,6,7,8,9,+,*,= 这 13 个数字和符号（称为现代算符）一一对应。为了便于标记，我们用 13 个小写英文字母 a,b,…m 代替这些符号（称为古梅算符）。但是，还没有人知道这些古梅算符和现代算符之间的具体对应关系。

### 输入描述

```
第一行为等式的个数 N，以下 N 行每行为一个等式。
每个等式的长度为 5 个字符到 11 个字符。
```
### 输出描述

```
如果不存在对应关系能够满足这组等式，输出noway。
如果有对应关系能够满足这组等式，输出所有能够确定的古梅算符和现代算符的对应关系。每一行有两个字符，其中第一个字符是古梅算符，第二个字符是对应的现代算符。输出按照字典顺序排序。
```

### 测试样例
#### 输入
```
2
abcdec
cdefe
```
#### 输出
```
a6
b*
d=
f+
```