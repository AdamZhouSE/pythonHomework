### 题目描述

读入一个由大小写英文字母或数字组成的字符串s，请把这个字符串分成若干部分s=s1s2s3...sm，使得每个si都是 Lyndon Word，且si>=s(i+1)。输出s1到sm这些串长度的右端点的位置。位置编号为1到n。

一个字符串s是一个 Lyndon Word 表示  是其所有后缀中的最小者。

### 输入描述

```
一行一个长度为n的仅包含大小写英文字母或数字的字符串 。
```
### 输出描述

```
一行若干个整数，第i个表示si的右端点在s中的位置。
```

### 测试样例
#### 输入
```
ababa

```
#### 输出
```
2 4 5
```
