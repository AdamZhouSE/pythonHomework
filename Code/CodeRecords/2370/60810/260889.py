'''
给出数字 N，返回由若干 "0" 和 "1"组成的字符串，该字符串为 N 的负二进制（base -2）表示。
除非字符串就是 "0"，否则返回的字符串中不能含有前导零。
'''

import math

n = int(input())
result = ""
while True:
    result = str(n % 2) + result
    n = math.ceil(n/-2)
    if n == 0:
        break
print(result) 