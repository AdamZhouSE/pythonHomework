### 题目描述
给定两个整数m＆n，找到长度为n的可能序列数，以使下一个元素中的每个元素大于或等于前一个元素的两倍但小于或等于m。
### 输入描述
第一行由测试用例T组成。每个测试用例的只有一行由2个整数M和N组成。
### 输出描述
单行输出可能的序列数
### 输入范例
```
2
10 4
5 2
```
### 输出范例
```
4
6
```
说明： 

输入：m = 10，n = 4 

输出4 应该有n个元素并且值last 元素最多应为m。 

序列为{1、2、4、8}，{1、2、4、9}， {1，2，4，10}，{1,2,5,10} 

输入：m = 5，n = 2 

输出6 

顺序为{1、2}，{1、3}，{1、4}， {1，5}，{2，4}，{2，5}
### 题目来源
geeksforgeeks.org

