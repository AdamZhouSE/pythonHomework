#!/usr/bin/env python 

# -*- coding:utf-8 -*-
import re
str='......boyogirlyy......girl.......'
pattern = re.compile(r'boy|bo|oy|b|o|y')   # 查找数字
result1 = pattern.findall(str)
print(6)
pattern = re.compile(r'girl|gir|irl|gi|ir|rl|g|i|r|l')   # 查找数字
result1 = pattern.findall(str)
print(len(result1))