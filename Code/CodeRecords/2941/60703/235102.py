#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 题目描述
# 高橋君正考虑在美国留学，并决定提交一份成绩单。 在美国留学的成绩表中，有必要标明gpa作为衡量学力的指标。 gpa是通过将每个单元的评估（a，b，c，d，f）转换成分数并转换成分数而获得的平均值如下。
#
# a评估→4分
#
# b评估→3分
#
# c评估→2分
#
# d评估→1分
#
# f评估→0分
#
# 如果全部f，gpa将为0。
#
# 输入描述
# 输入从标准输入中以以下形式输入
#
# N
#
# r1r2……rN
#
# 第一行是表示，总数N（1≦N≦100）。
#
# 第二行，给出了表示单位的评价的N个字的字符串。
#
# 第i个字ri是A，B，C，D，F中的任何一个。
# 输出描述
# 以输入和单位的评价为基础算出学业成绩从标准输出一行。
#
# 误差在1e-9以下（1-e9＝10^-9）
#
# 另外，输出要换行。
# 测试样例
# 输入
# 34
# ABABAAABACDDDABADFFABABDABFAAABFAA
# 输出
# 2.79411764705882

N=int(input());
Str = input();
sum=0;
for i in range(0,len(Str)):
    if(Str[i]=='A'):
        sum+=4;
    elif(Str[i]=='B'):
        sum+=3;
    elif (Str[i] == 'C'):
        sum += 2;
    elif (Str[i] == 'D'):
        sum += 1;
    elif (Str[i] == 'F'):
        sum += 0;
aver= sum/N;
if(aver==0.0):
    print(0,end="");
else:
    print(format(aver,'.14f'),end="");