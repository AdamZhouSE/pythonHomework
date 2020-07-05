#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
str='10'
pattern = re.compile(r'1+|0+')   # 查找数字
result1 = pattern.findall(str)
if '1' in result1[-1]:
    print(len(result1)-1)
else:
    print(len(result1))