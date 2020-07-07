### 题目描述

给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：


	子串中不同字母的数目必须小于等于 maxLetters 。
	子串的长度必须大于等于 minSize 且小于等于 maxSize 。

### 输入描述

```
一个字符串 s。二到四行分别是：maxLetters，minSize，maxSize
1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s 只包含小写英文字母。
```
### 输出描述

```
返回满足条件且出现次数最大的任意子串的出现次数
```

### 测试样例
#### 样例1: 输入-输出-解释
```
aababcaab
2
3
4
```
```
2
```
```
子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
```
### 题目来源  
`LeetCode`