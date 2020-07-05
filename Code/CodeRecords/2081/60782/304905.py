"""
题目描述

这是一道模板题。

给定一个字符串A和一个字符串B ，求B 在A中的出现次数。A 和B 中的字符均为英语大写字母或小写字母。

A 中不同位置出现的B 可重叠。

输入描述

输入共两行，分别是字符串A和字符串B 。

输出描述

输出一个整数，表示 B 在A 中的出现次数。
"""
# -- ecoding:utf-8 --
'''
转载和使用请保存此注释，欢迎私信评论交流
Please save this note for reprint and use.
作者（Author）：CSDN  清斋主人
'''


def is_change(strs, strs_cope, i, normal_num):
    # strs_cope中如果有元素等于strs[i]，那么就替换为normal_num，并返回替换了几次
    flag = 0
    for j in range(len(strs_cope)):
        if strs[i] == strs_cope[j]:
            strs_cope[j] = normal_num
            flag += 1
    return flag


def normalization(strs):
    # strs转换为列表，便于切片处理，这里strscope不能直接strs_cope=strs
    # 这样为浅拷贝，二者指向同一列表，这里需要的是一个strs的副本
    strs_ = list(strs)
    strscope = list(strs)
    normal_num = 0  # 方便起见，也为了不与a~z重复，替换为数字
    for i in range(len(strs_)):
        # 对于strs_cope循环判断所有元素是否等于strs[i]，也就是为了寻找所有相同的元素并进行替换
        # 如果替换了就将normal_num加1，为了在出现第二个不一样的元素时候替换为normal_num+1
        if (is_change(strs_, strscope, i, normal_num)):
            normal_num += 1
    return strscope


S = input()
T = input()
S = list(S)
T = normalization(T)
similar_num = 0
for i in range(len(S) - len(T) + 1):
    S_ = "".join(S[i:(len(T)) + i])  # 将列表转换为子串
    # print(S_)
    if normalization(S_) == T:  # 转换后判断是否相同
        similar_num += 1
print
similar_num
